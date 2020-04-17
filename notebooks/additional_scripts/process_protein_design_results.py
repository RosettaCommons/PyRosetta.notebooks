#!/usr/bin/env python
# @file: analyze_test4_protein_design.py
# @brief: Analyze protein design results by calculating sequence recovery and KL divergence
# @author: Rebecca F. Alford (ralford3@jhu.edu)

import sys, os
import numpy as np
from collections import defaultdict

from optparse import OptionParser, IndentedHelpFormatter
_script_path_ = os.path.dirname( os.path.realpath(__file__) )

residues = [ 'A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'Y' ]
categories = [ 'nonpolar', 'special', 'charged', 'charged', 'aromatic', 'special', 'charged', 'nonpolar', 'charged', 'nonpolar', 'nonpolar', 'polar', 'special', 'polar', 'charged', 'polar', 'polar', 'nonpolar', 'aromatic', 'aromatic' ]

def read_design_matrix( filename ): 

	with open( filename, 'rt' ) as f: 
		content = f.readlines()
		content = [ x.strip() for x in content ]
		content = [ x.split() for x in content ]

	design_matrix = defaultdict(list)
	for col in range(0, len(content[0]) ): 
		datatype = content[0][col]
		data = []
		for aa in range(1, 21): 
			if ( datatype != "Residue" ):
				data.append( float(content[aa][col]) )
			else: 
				data.append( content[aa][col] )
		design_matrix[ datatype ] = data

	return design_matrix

def read_design_calc_files( filename ): 

	with open( filename, 'rt' ) as f: 
		design_calc_list = f.readlines()
		design_calc_list = [ x.strip() for x in design_calc_list ]

	design_matrices = defaultdict(dict)
	for design_calc in design_calc_list:
		design_type = design_calc.strip(".txt")
		matrix = read_design_matrix( design_calc )
		design_matrices[ design_type ] = matrix 

	return design_matrices 
		
def aa_to_index( design_matrix, aa ): 
	return design_matrix[ 'Residue' ].index( aa )

def compute_total_recovery( design_matrix, category ): 

	if ( category == "all" ): 
		category = ""
	else: 
		category = "." + category

	category_correct = "No.correct" + category
	category_native = "No.native" + category
	n_correct = np.sum( np.array( design_matrix[ category_correct ] ) )
	n_native = np.sum( np.array( design_matrix[ category_native ] ) ) 
	return np.round( np.divide( n_correct, n_native ), 3 )

def compute_recovery_by_aa( design_matrix, category ): 

	if ( category == "all" ): 
		category = ""
	else: 
		category = "." + category

	category_correct = "No.correct" + category
	category_native = "No.native" + category
	n_correct = np.array( design_matrix[ category_correct ] )
	n_native = np.array( design_matrix[ category_native ] )
	n_native[n_native == 0] = 1
	return np.round( np.divide( n_correct, n_native ), 3 )

def compute_recovery_by_aa_subset( design_matrix, category, subset ): 

	if ( category == "all" ): 
		category = ""
	else: 
		category = "." + category

	category_correct = "No.correct" + category
	category_native = "No.native" + category

	correct = 0.0
	native = 0.0
	for aa in subset: 
		aa_correct = design_matrix[ category_correct ][ aa_to_index( design_matrix, aa ) ]
		aa_native = design_matrix[ category_native ][ aa_to_index( design_matrix, aa ) ]
		correct += aa_correct
		native += aa_native

	if ( native == 0.0 ): native = 1
	return np.round( correct/native, 3 )

def compute_recovery_by_aa_class( design_matrix, category ): 

	recovery_by_aa_class = {}
	
	# Curate stats for nonpolar amino acids (A, L, M, V, I)
	nonpolar_aas = [ "ALA", "LEU", "MET", "ILE", "VAL" ]
	nonpolar_recovery = compute_recovery_by_aa_subset( design_matrix, category, nonpolar_aas ) 
	recovery_by_aa_class[ "nonpolar" ] = nonpolar_recovery

	# Curate stats for polar amino acids (N, Q, S, T)
	polar_aas = [ "ASN", "GLN", "THR", "SER" ]
	polar_recovery = compute_recovery_by_aa_subset( design_matrix, category, polar_aas )
	recovery_by_aa_class[ "polar" ] = polar_recovery

	# Curate stats for negatively charged amino acids (D, E)
	neg_charged_aas = [ "ASP", "GLU","HIS", "LYS", "ARG" ]
	neg_charged_recovery = compute_recovery_by_aa_subset( design_matrix, category, neg_charged_aas )
	recovery_by_aa_class[ "charged" ] = neg_charged_recovery

	# Curate stats for aromatic amino acids (F, Y, W)
	aromatic_aas = [ "PHE", "TRP", "TYR" ]
	aromatic_recovery = compute_recovery_by_aa_subset( design_matrix, category, aromatic_aas )
	recovery_by_aa_class[ "aromatic" ] = aromatic_recovery

	# Curate stats for special case amino acids
	special_aas = [ "CYS", "GLY", "PRO" ]
	special_case_recovery = compute_recovery_by_aa_subset( design_matrix, category, special_aas )
	recovery_by_aa_class[ "special" ] = special_case_recovery

	return recovery_by_aa_class

def compute_total_divergence( design_matrix, category ): 

	if ( category == "all" ): 
		category = ""
	else: 
		category = "." + category

	category_designed = "No.designed" + category
	category_native = "No.native" + category
	n_designed = np.array( design_matrix[ category_designed ] )
	n_native = np.array( design_matrix[ category_native ] )
	n_designed[ n_designed == 0 ] = 0.00001
	n_native[ n_native == 0 ] = 0.00001
	divided = np.log( np.divide( n_native, n_designed ) )
	return np.round( -np.sum( divided ), 3 )

def compute_divergence_by_aa( design_matrix, category ): 

	if ( category == "all" ): 
		category = ""
	else: 
		category = "." + category

	category_designed = "No.designed" + category
	category_native = "No.native" + category
	n_designed = np.array( design_matrix[ category_designed ] )
	n_native = np.array( design_matrix[ category_native ] )
	n_designed[ n_designed == 0 ] = 0.00001
	n_native[ n_native == 0 ] = 0.00001
	return np.round( -np.log( np.divide( n_native, n_designed ) ), 3 )

def compute_divergence_by_aa_subset( design_matrix, category, subset ): 

	if ( category == "all" ): 
		category = ""
	else: 
		category = "." + category

	category_designed = "No.designed" + category
	category_native = "No.native" + category

	divergence = 0.0
	for aa in subset: 
		aa_designed = design_matrix[ category_designed ][ aa_to_index( design_matrix, aa ) ]
		aa_native = design_matrix[ category_native ][ aa_to_index( design_matrix, aa ) ]
		if ( aa_designed == 0 ): 
			aa_designed = 0.00001
		if ( aa_native == 0 ): 
			aa_native = 0.00001
		divergence += -np.log( aa_native/aa_designed )

	return np.round( divergence, 3 )

def compute_divergence_by_aa_class( design_matrix, category ): 

	divergence_by_aa_class = {}
	
	# Curate stats for nonpolar amino acids (A, L, M, V, I)
	nonpolar_aas = [ "ALA", "LEU", "MET", "ILE", "VAL" ]
	nonpolar_divergence = compute_divergence_by_aa_subset( design_matrix, category, nonpolar_aas ) 
	divergence_by_aa_class[ "nonpolar" ] = nonpolar_divergence

	# Curate stats for polar amino acids (N, Q, S, T)
	polar_aas = [ "ASN", "GLN", "THR", "SER" ]
	polar_divergence = compute_divergence_by_aa_subset( design_matrix, category, polar_aas )
	divergence_by_aa_class[ "polar" ] = polar_divergence

	# Curate stats for negatively charged amino acids (D, E)
	neg_charged_aas = [ "ASP", "GLU", "HIS", "LYS", "ARG" ]
	neg_charged_divergence = compute_divergence_by_aa_subset( design_matrix, category, neg_charged_aas )
	divergence_by_aa_class[ "charged" ] = neg_charged_divergence

	# Curate stats for aromatic amino acids (F, Y, W)
	aromatic_aas = [ "PHE", "TRP", "TYR" ]
	aromatic_divergence = compute_divergence_by_aa_subset( design_matrix, category, aromatic_aas )
	divergence_by_aa_class[ "aromatic" ] = aromatic_divergence

	# Curate stats for special case amino acids
	special_aas = [ "CYS", "GLY", "PRO" ]
	special_case_divergence = compute_divergence_by_aa_subset( design_matrix, category, special_aas )
	divergence_by_aa_class[ "special" ] = special_case_divergence

	return divergence_by_aa_class

def main( args ) : 

	# Read options from the command line
	parser = OptionParser(usage="usage %prog --energy_fxn franklin2019" )
	parser.set_description(main.__doc__)
	
	parser.add_option( '--energy_fxn', '-e', action="store", help="Energy function")
	parser.add_option( '--seqrecov_file', '-s', action="store", help="Sequence recovery file", )
	parser.add_option( '--basedir', '-b', action="store", help="config benchmark path")

	(options, args) = parser.parse_args(args=args[1:])
	global Options
	Options = options

	# Make one list of design calc files
	working_dir = Options.basedir #+ "data/" + Options.energy_fxn + "/sequence-recovery"
	os.chdir( working_dir )
	os.system( "ls " + Options.seqrecov_file + " > design_calcs.list" )

	# Read in all design calculation files
	design_calc_files = "design_calcs.list"
	design_matrices = read_design_calc_files( design_calc_files )

	# Analyze total sequence recovery of designed proteins (per-category)
	with open( "total_sequence_recovery.dat", 'w' ) as f: 
		f.write( "overall buried surface lipid_facing interfacial aqueous efxn\n" )
		for key in design_matrices: 
			overall_recov = compute_total_recovery( design_matrices[ key ], "all" )
			buried_recov = compute_total_recovery( design_matrices[ key ], "core" )
			surface_recov = compute_total_recovery( design_matrices[ key ], "surface" )
			lipid_facing_recov = compute_total_recovery( design_matrices[ key ], "lipid.facing" )
			interfacial_recov = compute_total_recovery( design_matrices[ key ], "interface" )
			aqueous_recov = compute_total_recovery( design_matrices[ key ], "aqueous" )
			f.write( str(overall_recov) + " " + str(buried_recov) + " " + str(surface_recov) + " " + str(lipid_facing_recov) + " " + str(interfacial_recov) + " " + str(aqueous_recov) + " " + str(key) + "\n" )

	# Analyze per-aa sequence recovery of designed proteins (per-category)
	with open( "per_amino_acid_recovery.dat", 'w' ) as f: 
		f.write( "residue category overall buried surface lipid_facing interfacial aqueous efxn\n" )
		for key in design_matrices: 
			overall_recov = compute_recovery_by_aa( design_matrices[ key ], "all" )
			buried_recov = compute_recovery_by_aa( design_matrices[ key ], "core" )
			surface_recov = compute_recovery_by_aa( design_matrices[ key ], "surface" )
			lipid_facing_recov = compute_recovery_by_aa( design_matrices[ key ], "lipid.facing" )
			interfacial_recov = compute_recovery_by_aa( design_matrices[ key ], "interface" )
			aqueous_recov = compute_recovery_by_aa( design_matrices[ key ], "aqueous" )

			for ii in range(0, len(overall_recov)):
				f.write( residues[ ii ] + " " + categories[ii] + " " + str(overall_recov[ii]) + " " + str(buried_recov[ii]) + " " + str(surface_recov[ii]) + " " + str(lipid_facing_recov[ii]) + " " + str(interfacial_recov[ii]) + " " + str(aqueous_recov[ii]) + " " + str(key) + "\n" )

	# Analyze per-aa class recovery of designed proteins
	with open( "per_amino_acid_class_recovery.dat", 'w' ) as f: 
		f.write( "class overall buried surface lipid_facing interfacial aqueous efxn\n" )
		for key in design_matrices: 
			overall_recov = compute_recovery_by_aa_class( design_matrices[ key ], "all" )
			buried_recov = compute_recovery_by_aa_class( design_matrices[ key ], "core" )
			surface_recov = compute_recovery_by_aa_class( design_matrices[ key ], "surface" )
			lipid_facing_recov = compute_recovery_by_aa_class( design_matrices[ key ], "lipid.facing" )
			interfacial_recov = compute_recovery_by_aa_class( design_matrices[ key ], "interface" )
			aqueous_recov = compute_recovery_by_aa_class( design_matrices[ key ], "aqueous" )

			for class_key in overall_recov: 
				f.write( class_key + " " + str(overall_recov[class_key]) + " " + str(buried_recov[class_key]) + " " + str(surface_recov[class_key]) + " " + str(lipid_facing_recov[class_key]) + " " + str(interfacial_recov[class_key]) + " " + str(aqueous_recov[class_key]) + " " + key + "\n" )


	# Analyze total sequence divergence of designed proteins (per-category)
	with open( "total_sequence_divergence.dat", 'w' ) as f: 
		f.write( "overall buried surface lipid_facing interfacial aqueous efxn\n" )
		for key in design_matrices: 
			overall_div = compute_total_divergence( design_matrices[ key ], "all" )
			buried_div = compute_total_divergence( design_matrices[ key ], "core" )
			surface_div = compute_total_divergence( design_matrices[ key ], "surface" )
			lipid_facing_div = compute_total_divergence( design_matrices[ key ], "lipid.facing" )
			interfacial_div = compute_total_divergence( design_matrices[ key ], "interface" )
			aqueous_div = compute_total_divergence( design_matrices[ key ], "aqueous" )
			f.write( str(overall_div) + " " + str(buried_div) + " " + str(surface_div) + " " + str(lipid_facing_div) + " " + str(interfacial_div) + " " + str(aqueous_div) + " " + str(key) + "\n" )

	# Analyze per-aa sequence divergence of designed proteins (per-category)
	with open( "per_amino_acid_divergence.dat", 'w' ) as f: 
		f.write( "residue category overall buried surface lipid_facing interfacial aqueous efxn\n" )
		for key in design_matrices: 
			overall_div = compute_divergence_by_aa( design_matrices[ key ], "all" )
			buried_div = compute_divergence_by_aa( design_matrices[ key ], "core" )
			surface_div = compute_divergence_by_aa( design_matrices[ key ], "surface" )
			lipid_facing_div = compute_divergence_by_aa( design_matrices[ key ], "lipid.facing" )
			interfacial_div = compute_divergence_by_aa( design_matrices[ key ], "interface" )
			aqueous_div = compute_divergence_by_aa( design_matrices[ key ], "aqueous" )

			for ii in range(0, len(overall_div)):
				f.write( residues[ ii ] + " " + categories[ii] + " " + str(overall_div[ii]) + " " + str(buried_div[ii]) + " " + str(surface_div[ii]) + " " + str(lipid_facing_div[ii]) + " " + str(interfacial_div[ii]) + " " + str(aqueous_div[ii]) + " " + str(key) + "\n" )

	# Analyze per-aa class divergence of designed proteins
	with open( "per_amino_acid_class_divergence.dat", 'w' ) as f: 
		f.write( "class overall buried surface lipid_facing interfacial aqueous efxn\n" )
		for key in design_matrices: 
			overall_div = compute_divergence_by_aa_class( design_matrices[ key ], "all" )
			buried_div = compute_divergence_by_aa_class( design_matrices[ key ], "core" )
			surface_div = compute_divergence_by_aa_class( design_matrices[ key ], "surface" )
			lipid_facing_div = compute_divergence_by_aa_class( design_matrices[ key ], "lipid.facing" )
			interfacial_div = compute_divergence_by_aa_class( design_matrices[ key ], "interface" )
			aqueous_div = compute_divergence_by_aa_class( design_matrices[ key ], "aqueous" )

			for class_key in overall_div: 
				f.write( class_key + " " + str(overall_div[class_key]) + " " + str(buried_div[class_key]) + " " + str(surface_div[class_key]) + " " + str(lipid_facing_div[class_key]) + " " + str(interfacial_div[class_key]) + " " + str(aqueous_div[class_key]) + " " + key + "\n" )

if __name__ == "__main__" : main(sys.argv)

