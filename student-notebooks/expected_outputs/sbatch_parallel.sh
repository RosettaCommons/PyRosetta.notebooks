#!/bin/bash 
#SBATCH -p short 
#SBATCH -n 8 
#SBATCH -N 1 
#SBATCH --mem=16g 
#SBATCH -o sbatch_parallel.log 
conda activate pyrosetta-bootcamp 
cat outputs/run_file_parallel_interactive.txt | /usr/bin/parallel -j 8 --no-notice 
