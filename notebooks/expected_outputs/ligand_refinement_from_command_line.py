import optparse
import os
import pyrosetta


def sample_ligand_interface(pdb_filename,
                            partners,
                            ligand_params=[""],
                            jobs=1,
                            job_output="ligand_output"):
    """
    Performs ligand-protein docking using Rosetta fullatom docking
    (DockingHighRes) on the ligand-protein complex in  <pdb_filename>
    using the relative chain  <partners>. If the ligand parameters
    (a .params file) are not defaultly loaded into PyRosetta,
    <ligand_params> must supply the list of files including the ligand
    parameters. <jobs>  trajectories are performed with output
    structures named <job_output>_(job#).pdb.
    
    Note: Global docking, a problem solved by the Rosetta DockingProtocol,
    requires interface detection and refinement as with other protocols,
    these tasks are split into centroid (interface detection) and
    high-resolution (interface refinement) methods without a centroid 
    representation, low-resolution ligand-protein prediction is not
    possible and as such, only the high-resolution ligand-protein 
    interface refinement is available. If you add a perturbation or 
    randomization step, the high-resolution stages may fail. A perturbation
    step CAN make this a global docking algorithm however the rigid-body
    sampling preceding refinement requires extensive sampling to produce
    accurate results and this algorithm spends most of its effort in
    refinement (which may be useless for the predicted interface).
    
    This script performs ligand-protein interface structure prediction but does NOT
    perform global ligand-protein docking. Since there is no generic interface
    detection, the input PDB file must have the ligand placed near the interface
    that will be refined. If the DockMCMProtocol is applied to a pose
    without placement near the interface, then the refinement may:
        -waste steps sampling the wrong interface
        -fail by predicting an incorrect interface very far from the true interface
        -fail by separating the ligand from the protein (usually due to a clash)
    DockMCMProtocol does not require an independent randomization or perturbation
    step to "seed" its prediction.
    
    Additional refinement steps may increase the accuracy of the predicted
    conformation (see refinement.py). Drastic moves (large conformational changes)
    should be avoided; if they precede the protocol, the problems above may occur,
    if they succeed the protocol, the protocol results may be lost.
    """

    # Declare working directory and output directory
    working_dir = os.getcwd()
    output_dir = "outputs"
    if not os.path.exists(output_dir):
        os.mkdir(output_dir)
    
    # Initialize PyRosetta
    pyrosetta.init()
    
    # Create an empty pose from the desired PDB file
    pose = pyrosetta.rosetta.core.pose.Pose()

    # If the params list has contents, load .params files
    # Note: this method of adding ligands to the ResidueTypeSet is unnecessary
    # if you call pyrosetta.init("-extra_res_fa {}".format(ligand_params))
    if len(ligand_params) != 0 and ligand_params[0] != "":
        ligand_params = pyrosetta.Vector1(ligand_params)
        res_set = pose.conformation().modifiable_residue_type_set_for_conf()
        res_set.read_files_for_base_residue_types(ligand_params)
        pose.conformation().reset_residue_type_set_for_conf(res_set)
    
    # Load pdb_filename into pose
    pyrosetta.io.pose_from_file(pose, pdb_filename)

    # Setup the docking FoldTree
    # the method setup_foldtree takes an input pose and sets its
    #    FoldTree to have jump 1 represent the relation between the two docking
    #    partners, the jump points are the residues closest to the centers of
    #    geometry for each partner with a cutpoint at the end of the chain,
    # the second argument is a string specifying the relative chain orientation
    #    such as "A_B" of "LH_A", ONLY TWO BODY DOCKING is supported and the
    #    partners MUST have different chain IDs and be in the same pose (the
    #    same PDB), additional chains can be grouped with one of the partners,
    #    the "_" character specifies which bodies are separated
    # the third argument...is currently unsupported but must be set (it is
    #    supposed to specify which jumps are movable, to support multibody
    #    docking...but Rosetta doesn't currently)
    # the FoldTrees setup by this method are for TWO BODY docking ONLY!
    dock_jump = 1 # jump number 1 is the inter-body jump
    pyrosetta.rosetta.protocols.docking.setup_foldtree(pose,
                                                       partners,
                                                       pyrosetta.Vector1([dock_jump]))

    # Create a copy of the pose for testing
    test_pose = pose.clone()

    # Create ScoreFunctions for centroid and fullatom docking
    scorefxn = pyrosetta.create_score_function("ligand")

    # Setup the high resolution (fullatom) docking protocol using DockMCMProtocol.
    docking = pyrosetta.rosetta.protocols.docking.DockMCMProtocol()
    # Many of its options and settings can be set using the setter methods.
    docking.set_scorefxn(scorefxn)

    # Change directory temporarily for output
    os.chdir(output_dir)
    
    # Setup the PyJobDistributor
    jd = pyrosetta.toolbox.py_jobdistributor.PyJobDistributor(job_output,
                                                              jobs, scorefxn,
                                                              compress=False)

    # Set the native pose so that the output scorefile contains the pose rmsd metric
    jd.native_pose = pose 
    
    # Optional: setup a PyMOLObserver
    # pyrosetta.rosetta.protocols.moves.AddPyMOLObserver(test_pose, True)

    # Perform protein-ligand docking
    # counter = 0 # for pretty output to PyMOLObserver
    
    while not jd.job_complete:
        test_pose = pose.clone() # Reset test pose to original structure
        
        # counter += 1 # Change the pose name, for pretty output to PyMOLObserver
        # test_pose.pdb_info().name(job_output + '_' + str(counter))
        
        docking.apply(test_pose) # Perform docking and output to PyMOL

        # Write the decoy structure to disc
        jd.output_decoy(test_pose)
    
    os.chdir(working_dir)

if __name__ == "__main__":
    
    # Declare parser object for managing input options
    parser = optparse.OptionParser()
    parser.add_option("--pdb_filename",
                      dest="pdb_filename",
                      help="The PDB file containing the ligand and protein to dock.")
    parser.add_option("--partners", 
                      dest="partners",
                      default = "A_X",
                      help="The relative chain partners for docking.")
    parser.add_option("--ligand_params",
                      dest="ligand_params",
                      help="The ligand residue parameter file.")
    parser.add_option("--jobs", 
                      dest="jobs",
                      default="1",
                      help="The number of jobs (trajectories) to perform.")
    parser.add_option("--job_output", 
                      dest="job_output",
                      default = "ligand_output",
                      help="The name preceding all output, output PDB files and scorefile.")
    (options, args) = parser.parse_args()
    
    # Catch input erros
    if not options.pdb_filename:
        parser.error("pdb_filename not given!")
    if not options.ligand_params:
        parser.error("ligand_params not given!")

    # Run ligand refinement protocol
    sample_ligand_interface(pdb_filename=options.pdb_filename,
                            partners=options.partners,
                            ligand_params=options.ligand_params.split(","),
                            jobs=int(options.jobs),
                            job_output=options.job_output)
