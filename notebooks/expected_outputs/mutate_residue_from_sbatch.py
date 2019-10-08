#!/home/klimaj/anaconda3/envs/pyrosetta-bootcamp/bin/python
#SBATCH -p short
#SBATCH -n 1
#SBATCH --mem=2g
#SBATCH -o sbatch.log

import argparse
import os
import pyrosetta
import uuid


__author__ = "My Name"
__email__ = "name@email.com"


def main(target=None, new_res=None):
    """Example function to run my custom PyRosetta script.
    """
    
    # Initialize PyRosetta with custom flags
    pyrosetta.init("-ignore_unrecognized_res 1 -renumber_pdb 1 -mute all")

    # Setup pose
    pose = pyrosetta.pose_from_file("inputs/5JG9.clean.pdb")
    
    # Setup directory structure
    main_dir = os.getcwd()
    unique_dir = os.path.join("outputs", "testing_" + uuid.uuid4().hex)
    if not os.path.isdir(unique_dir):
        os.mkdir(unique_dir)
        os.chdir(unique_dir)

    # Create scorefunction
    scorefxn = pyrosetta.create_score_function("ref2015_cart")

    # PyRosetta design protocol
    keep_chA = pyrosetta.rosetta.protocols.grafting.simple_movers.KeepRegionMover(
        res_start=str(pose.chain_begin(1)), res_end=str(pose.chain_end(1))
    )
    keep_chA.apply(pose)
    
    mutate = pyrosetta.rosetta.protocols.simple_moves.MutateResidue(
        target=target, new_res=new_res
    )
    mutate.apply(pose)

    mm = pyrosetta.rosetta.core.kinematics.MoveMap()
    mm.set_bb(True)
    mm.set_chi(True)
    min_mover = pyrosetta.rosetta.protocols.minimization_packing.MinMover()
    min_mover.set_movemap(mm)
    min_mover.score_function(scorefxn)
    min_mover.min_type("lbfgs_armijo_nonmonotone")
    min_mover.cartesian(True)
    min_mover.tolerance(0.01)
    min_mover.max_iter(200)
    min_mover.apply(pose)

    total_score = scorefxn(pose)
    
    # Setup outputs
    pdb_output_filename = "_".join(["5JG9.clean", str(target), str(new_res), ".pdb"])
    
    pyrosetta.dump_pdb(pose, pdb_output_filename)
    
    # Append scores to scorefile
    pyrosetta.toolbox.py_jobdistributor.output_scorefile(
        pose=pose, pdb_name="5JG9.clean", current_name=pdb_output_filename,
        scorefilepath="score.fasc", scorefxn=scorefxn,
        nstruct=1, native_pose=None, additional_decoy_info=None, json_format=True
    )
    os.chdir(main_dir)

    
if __name__ == "__main__":
    
    # Declare parser object for managing input options
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--target", type=int,
                    help="Target residue to mutate as integer.")
    parser.add_argument("-r", "--new_res", type=str,
                        help="Three letter amino acid code to which to mutate target.")
    args = parser.parse_args()
    
    # Run protocol
    main(target=args.target, new_res=args.new_res)
