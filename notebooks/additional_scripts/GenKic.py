from pyrosetta.rosetta.protocols.generalized_kinematic_closure import GeneralizedKIC
from pyrosetta import create_score_function
from pyrosetta.rosetta.utility import vector1_core_id_NamedAtomID
from pyrosetta.rosetta.core.id import NamedAtomID


class GenKic:
    def __init__(self, loop_residues):
        """VK Mulligans insanely customizable GenKic algorithm adapted to PyRosetta

        Arguments:
            loop_residues {list} -- list of pose residues that will be rebuilt in the GenKic Protocol

        it is imperative that you read V. Mulligan tutorials to have any idea what the hell is going on. Currently this is behind
        the RosettaCommons Firwall
        https://github.com/RosettaCommons/demos/blob/master/tutorials/GeneralizedKIC/generalized_kinematic_closure_1.md

        """
        # Make an Instance
        self.gk_instance = GeneralizedKIC()

        # Pose Numbering of residues to consider in the GK. Can be a loop or the entire structure
        self.loop_residues = loop_residues
        for res_num in self.loop_residues:
            self.gk_instance.add_loop_residue(res_num)

        # The residues to pivot around GK. These of scourse can be reset, but you should use the defaults
        self.pivot_residues = [
            self.loop_residues[0],
            self.loop_residues[int(len(self.loop_residues) / 2)],
            self.loop_residues[-1],
        ]

        # Here are some basics we can set in the constructor but also have the option to set somewhere else
        self.closure_attempts = 100000
        self.min_solutions = 1
        self.scorefxn = create_score_function("ref2015")

        self.selector = ""
        # # Defaults
        # # 1. Make sure PIVOT atoms obey rama space
        # self.filter_pivot = True

        # # 2. Make the loop not bump into itself, i'm not sure why it would ever be off
        # self.filter_loop_bump = True

    """ Setters that have a Default """

    def set_loop_residues(self, loops):
        """set_loop_residues Sets Loop Residues that are being considerd in GK

        Arguments:
            loops {list} -- List of pose residues to consider
        """
        self.loop_residues = loop_residues
        for res_num in self.loop_residues:
            self.gk_instance.add_loop_residue(res_num)

    def set_pivot_residues(self, p_residues):
        """set_pivot_residues resets the pivot residues

        Arguments:
            p_residues {list} -- List of three pivot residues which have to be in the loop to be considerd
        """

        self.pivot_residues = p_residues
        assert len(self.pivot_residues) == 3

    def get_pivot_residues(self):
        return self.pivot_residues

    def set_closure_attempts(self, closure_attempts):
        """set_closure_attempts How many times should we attempt gen kic

        Arguments:
            closure_attempts {int}
        """
        self.closure_attempts = closure_attempts

    def set_min_solutions(self, count):
        """set_min_solutions GenKic will stop trying after this many successful closures

        Arguments:
            count {int}
        """
        self.min_solutions = count

    def set_scorefxn(self, s):
        """set_scorefxn set an alternative scorefunciton, defaults to ref2015

        Arguments:
            s {pyrosetta.scorefunction} -- A scorefunction object
        """
        self.scorefxn = s

    def set_filter_pivot(self, b):
        """set_filter_pivot Turn off the automatic filter that checks your pivot residues to make sure
        they don't violate rama space

        Arguments:
            b {bool} -- Turn on/off filter pivot
        """

        self.filter_pivot = b

    def set_selector_type(self,s):
        if s not in self.get_gk_selectors():
            raise Exception('{} not in {}'.format(self.get_gk_selectors()))
        else:
            self.selector = s

    def get_gk_selectors(self):
        return [
            "no_selector",
            "random_selector",
            "lowest_energy_selector",
            "boltzmann_energy_selector",
            "lowest_rmsd_selector",
            "lowest_delta_torsion_selector",
        ]

    def get_gk_perturbors(self):
        return [
            "set_dihedral",
            "set_bondangle",
            "set_bondlength",
            "set_backbone_bin",
            "randomize_dihedral",
            "randomize_alpha_backbone_by_rama",
            "randomize_backbone_by_rama_prepro",
            "randomize_backbone_by_bins",
            "perturb_dihedral",
            "perturb_dihedral_bbg",
            "perturb_backbone_by_bins",
            # "copy_backbone_dihedrals",
            # "mirror_backbone_dihedrals",
            # "sample_cis_peptide_bond",
        ]

    def get_gk_filters(self):
        return ["loop_bump_check",
                "atom_pair_distance",
                "backbone_bin",
                "alpha_aa_rama_check",
                "rama_prepro_check"]

    """Perturbers"""

    def set_dihedral(self, r1, r2, a1, a2, d):
        """set_dihedral [summary]

        Arguments:
            r1 {[type]} -- [description]
            r2 {[type]} -- [description]
            a1 {[type]} -- [description]
            a2 {[type]} -- [description]
            d {[type]} -- [description]
        """
        #print("Setting Dihedrals")
        self.gk_instance.add_perturber("set_dihedral")
        atomset = vector1_core_id_NamedAtomID()
        atomset.append(NamedAtomID(a1, r1))
        atomset.append(NamedAtomID(a2, r2))
        self.gk_instance.add_atomset_to_perturber_atomset_list(atomset)
        self.gk_instance.add_value_to_perturber_value_list(d)

    def set_bondangle(self, r1, r2, a1, a2, d):
        """set_bondangle [summary]

        Arguments:
            r1 {[type]} -- [description]
            r2 {[type]} -- [description]
            a1 {[type]} -- [description]
            a2 {[type]} -- [description]
            d {[type]} -- [description]
        """
        print("Setting Bond angle")
        self.gk_instance.add_perturber("set_bondangle")
        atomset = vector1_core_id_NamedAtomID()
        atomset.append(NamedAtomID(a1, r1))
        atomset.append(NamedAtomID(a2, r2))
        self.gk_instance.add_atomset_to_perturber_atomset_list(atomset)
        self.gk_instance.add_value_to_perturber_value_list(d)

    def set_bondlength(self, r1, r2, a1, a2, d):
        """set_bondlength [summary]

        Arguments:
            r1 {[type]} -- [description]
            r2 {[type]} -- [description]
            a1 {[type]} -- [description]
            a2 {[type]} -- [description]
            d {[type]} -- [description]
        """
        print("Setting Bond Lengths")
        self.gk_instance.add_perturber("set_bondlength")
        atomset = vector1_core_id_NamedAtomID()
        atomset.append(NamedAtomID(a1, r1))
        atomset.append(NamedAtomID(a2, r2))
        self.gk_instance.add_atomset_to_perturber_atomset_list(atomset)
        self.gk_instance.add_value_to_perturber_value_list(d)

    def set_backbone_bin(self, r, b, bin="ABEGO"):
        """set_backbonebin [summary]

        Arguments:
            r {[type]} -- [description]
            b {[type]} -- [description]

        Keyword Arguments:
            bin {str} -- [description] (default: {'ABEGO'})

        From VK:

        Randomly select mainchain torsions from within a mainchain torsion bin (effect="set_backbone_bin")
        This perturber takes a user-specified bin and bin transitions probability file, and randomly chooses 
        mainchain torsions for specified residues from within that bin. 
        The perturber has two additional input options: a bin transitions probability file
        """

        self.gk_instance.add_perturber("set_backbone_bin")
        self.gk_instance.add_residue_to_perturber_residue_list(r)
        self.gk_instance.load_perturber_bin_params(bin)
        self.gk_instance.set_perturber_bin(b)

    def randomize_dihedral(self, r1, r2, a1, a2):
        """randomize_dihedral 
        This perturber assigns each specified dihedral angle a uniformly-distributed 
        random value between -180 degrees and 180 degrees. The value from the input structure is discarded. 
        Dihedral angles are specified with AddAtoms blocks, and are defined by either two or four atoms. 

        Arguments:
            r1 {[type]} -- [description]
            r2 {[type]} -- [description]
            a1 {[type]} -- [description]
            a2 {[type]} -- [description]
        """

        self.gk_instance.add_perturber("randomize_dihedral")
        atomset = vector1_core_id_NamedAtomID()
        atomset.append(NamedAtomID(a1, r1))
        atomset.append(NamedAtomID(a2, r2))
        self.gk_instance.add_atomset_to_perturber_atomset_list(atomset)

    def randomize_alpha_backbone_by_rama(self, r, custom_rama_table=""):
        """randomize_dihedral 
            This perturber operates on residues specified with AddResidue blocks. 
            It randomizes backbone phi and psi angles biased by each residue's preferred regions within the Ramachandran plot. 
            It works on alpha-L and alpha-D amino acids. At least one of the backbone dihedral angles must be part of the chain to be closed. 
            ptionally, the user may specify a custom Ramachandran plot for sampling using the custom_rama_table=<string> option within the AddPerturber block. 
            Currently-supported custom Ramachandran plots include: 
            flat_l_aa_ramatable, flat_d_aa_ramatable, flat_symm_dl_aa_ramatable, flat_symm_gly_ramatable, 
            flat_symm_pro_ramatable, flat_l_aa_ramatable_stringent, flat_d_aa_ramatable_stringent, flat_symm_dl_aa_ramatable_stringent,
            flat_symm_gly_ramatable_stringent, and flat_symm_pro_ramatable_stringent. 

            Arguments:
                r1 {[type]} -- [description]
                r2 {[type]} -- [description]
                a1 {[type]} -- [description]
                a2 {[type]} -- [description]
            """

        self.gk_instance.add_perturber("randomize_alpha_backbone_by_rama")
        self.gk_instance.add_residue_to_perturber_residue_list(r)
        if custom_rama_table:
            self.gk_instance.set_perturber_custom_rama_table(custom_rama_table)

    def randomize_backbone_by_rama_prepro(self, r):
        """randomize_alpha_backbone_by_ramsa
            Randomize backbone dihedral angles, biased by the new Ramachandran plots that the rama_prepro energy term uses.
            This perturber operates on residues specified with AddResidue blocks. Like the randomize_alpha_backbone_by_rama perturber, 
            it randomizes mainchain torsion angles biased by Ramachandran maps in the database. However, it has several advantages over 
            randomize_alpha_backbone_by_rama. First, it is not limited to canonical alpha-amion acids, but can work with any polymer type for which Ramachandran maps are available. Second, it works with residue types with any number of rotatable mainchain torsions (i.e. it is not limited to two-dimensional Ramachandran maps). Third, it uses a different Ramachandran map at positions preceding N-substitued positions 
            (L-proline, D-proline, N-methylated amino acids, peptoids, etc.), better capturing the steric effects of the next residue's N-substitution on conformation. 
        Arguments:
            r {[type]} -- [description]
        """
        self.gk_instance.add_perturber("randomize_backbone_by_rama_prepro")
        self.gk_instance.add_residue_to_perturber_residue_list(r)

    def randomize_backbone_by_bins(self, r_stretch, bin="ABEGO"):
        """
        randomize_backbone_by_bins Randomize mainchain torsions based on torsion bin transition probabilities (effect="randomize_backbone_by_bins")
        This perturber will take a contiguous stretch of heteropolymer backbone and randomize it in a biased manner, based on the relative probabilities 
        of transitioning from one torsion bin to another. 
        """
        self.gk_instance.add_perturber("randomize_backbone_by_bins")
        for r in r_stretch:
            self.gk_instance.add_residue_to_perturber_residue_list(r)
        self.gk_instance.load_perturber_bin_params(bin)

    def perturb_dihedral(self, r1, r2, a1, a2, d):
        """perturb_dihedral This perturber adds a small, Gaussian-distributed value to each dihedral value specified. 
        Backbone dihedral values are specified using AddAtoms blocks, with two or four atoms listed in each. At least one AddValue block is required, 
        with the value specifying the width of the Gaussian (in degrees). If more than one AddValue block is specified, one must be listed for each AddAtoms block;
        this permits different perturbation sizes for different dihedral angles. 
        Unlike the randomize_dihedral perturber, the input dihedral values are preserved by this perturber, with a small random value added or subtracted to each.

        Arguments:
            r1 {[type]} -- [description]
            r2 {[type]} -- [description]
            a1 {[type]} -- [description]
            a2 {[type]} -- [description]
        """
        self.gk_instance.add_perturber("perturb_dihedral")
        atomset = vector1_core_id_NamedAtomID()
        atomset.append(NamedAtomID(a1, r1))
        atomset.append(NamedAtomID(a2, r2))
        self.gk_instance.add_atomset_to_perturber_atomset_list(atomset)
        self.gk_instance.add_value_to_perturber_value_list(d)

    def perturb_dihedral_bbg(self, r):
        """perturb_dihedral_bbg This perturber uses the backbone Gaussian mover to perturb the loop. 
        The backbone Gaussian mover introduces larger backbone motions, then uses some rapid minimization to 
        minimize the distance that the last residue moves. This results in a large perturbation to the middle of the loop, 
        and a small gap that GeneralizedKIC must subsequently close. Residues are specified with AddResidue tags; no values are required.

        Arguments:
            r {[type]} -- [description]
        """
        self.gk_instance.add_perturber("perturb_dihedral")
        self.gk_instance.add_residue_to_perturber_residue_list(r)

    def perturb_backbone_by_bins(self, r_stretch, bin="ABEGO", iteration=1, switch=False):
        self.gk_instance.add_perturber("perturb_backbone_by_bins")
        self.gk_instance.set_perturber_iterations(iteration)
        self.gk_instance.load_perturber_bin_params(bin)
        self.gk_instance.set_perturber_must_switch_bins(switch)

    """Filters"""
    def set_filter_loop_bump_check(self):
        """set_loop_bump_check 
        This applies a very simple, low-stringency bump check to each solution found, discarding solutions with obvious clashes. 
        The check is done in two steps. First, every atom in the chain of atoms to be closed is checked against every other 
        (with clashes between atoms in the same or adjacent residues ignored). Second, every atom in the chain of atoms to be closed 
        is checked against every mainchain atom (and, in the case of alpha- and beta-amino acids, beta carbon atoms) in every residue that is 
        not in the loop to be closed. which is not directly connected to the loop to be closed, 
        and which is not a tail residue. Note that tail residues are never checked for clashes. This filter takes no parameters, and has no shorthand.
        """
        self.gk_instance.add_filter("loop_bump_check")

    def set_filter_atom_pair_distance(self, r1, r2, a1, a2, d, gt=False):
        """set_atom_pair_distanceAtom pair distance (type="atom_pair_distance")
        This discards any solution in which two specified atoms are not within a distance threshold specified
         with a Real parameter called distance. The atoms are specified with two string parameters called atom1 and atom2, 
         and two integer-valued parameters called res1 and res2. If a Boolean parameter called greater_than is set to true, 
         this filter will discard any solution in which the two specified atoms are not separated by at least the distance specified.
          Because this filter takes several parameters, a shorthand exists (see below). 

        Arguments:
            r1 {[type]} -- [description]
            r2 {[type]} -- [description]
            a1 {[type]} -- [description]
            a2 {[type]} -- [description]
            d {[type]} -- [description]

        Keyword Arguments:
            gt {bool} -- [description] (default: {False})
        """
        self.gk_instance.add_filter("atom_pair_distance")
        self.gk_instance.add_filter_parameter("atom1", a1)
        self.gk_instance.add_filter_parameter("atom2", a2)
        self.gk_instance.add_filter_parameter("res1", r1)
        self.gk_instance.add_filter_parameter("res2", r2)
        self.gk_instance.add_filter_parameter("distance", d)
        if gt:
            self.gk_instance.add_filter_parameter("greater_than", True)

    def set_filter_backbone_bin(self, r, b, bin='ABEGO'):
        """set_filter_backbone_bin Residue mainchain torsion bin (type="backbone_bin")
        This filter checks that a given residue's mainchain torsion values lie within a desired mainchain torsion bin. This filter takes three additional parameters: a residue number (residue=(&int)), a bin transition probabilities file (bin_params_file=(&string "ABBA.bin_params")), and a bin name (bin=(&string)).

        Arguments:
            r {[type]} -- [description]
            b {[type]} -- [description]

        Keyword Arguments:
            bin {str} -- [description] (default: {'ABEGO'})
        """
        self.gk_instance.add_filter("backbone_bin")
        self.gk_instance.set_filter_resnum(r)
        self.gk_instance.load_filter_bin_params(bin)
        self.gk_instance.set_filter_bin(b)

    def set_filter_alpha_aa_rama_check(self, r):
        """set_filter_alpha_aa_rama_check [summary]

        Arguments:
            r {[type]} -- [description]
        """
        self.gk_instance.add_filter("alpha_aa_rama_check")
        self.gk_instance.set_filter_resnum(r)

    def set_filter_rama_prepro(self, r, cutoff=1.0):
        """set_filter_rama_prepro This filter checks that the rama_prepro energy of a given polymeric residue is below a set threshold. The rama_prepro energy is a mainchain torsion score similar to the older rama energy, albeit with several advantages. First, it can be defined for arbitrary polymeric residue types, and not just for canonical alpha-amino acids. Second, it is not limited to residue types with two mainchain torsions (e.g. alpha-amino acids), but can be applied to arbitrary residue types (beta-amino acids, gamma-amino acids, etc.), provided that N-dimensional Ramachandran tables exist for them. Third, a different Ramachandran map is used for a given residue type appearing before a proline residue (or other N-substituted residue type) in lindear sequence, allowing the effects on conformational preferences ofthe N-substitution to be taken into account. This filter also uses the rama_cutoff_energy option to specify the filtering threshold.

        Arguments:
            r {[type]} -- [description]

        Keyword Arguments:
            cutoff {float} -- [description] (default: {1.0})
        """
        self.gk_instance.add_filter("rama_prepro_check")
        self.gk_instance.set_filter_resnum(r)
        self.gk_instance.set_filter_rama_cutoff_energy(cutoff)

    """Conveincince Functions"""

    def set_omega_angles(self, omega_value=180):
        """set_omega_angles [summary]

       Keyword Arguments:
           omega_value {int} -- [description] (default: {180})
       """
        for res_num in self.loop_residues[:-1]:
            self.set_dihedral(res_num, res_num + 1, "C", "N", omega_value)

    def close_normal_bond(self, r1, r2):
        self.gk_instance.close_bond(
            r1,
            "C",
            r2,
            "N",
            r1,
            "CA",
            r2,
            "CA",
            1.32829,  # ideal bond length
            116.2,  # ideal bond angle 1 N-C-CA
            121.7,  # ideal bond angle 2 CA-N-C
            180.0,
            False,
            False,
        )

    def perturb_dihedra_by_res(self, r, d):
        # PHI
        # C(-1)-N-Cα-C
        self.perturb_dihedral(r, r, 'N', 'CA', d)
        self.perturb_dihedral(r, r, 'CA', 'C', d)

    def get_instance(self):
        """Get the instance back with everything set"""
        # Selector
        if self.selector:
            self.gk_instance.set_selector_type(self.selector)

        else:
            return self.get_gk_selectors()

        # Set closure attempts
        self.gk_instance.set_closure_attempts(self.closure_attempts)

        # Set N solutions
        self.gk_instance.set_min_solution_count(self.min_solutions)

        # Set selector scorefunction
        self.gk_instance.set_selector_scorefunction(self.scorefxn)

        # ADD PIVOT ATOMS
        self.gk_instance.set_pivot_atoms(
            self.pivot_residues[0],
            "CA",
            self.pivot_residues[1],
            "CA",
            self.pivot_residues[2],
            "CA",
        )
        return self.gk_instance
