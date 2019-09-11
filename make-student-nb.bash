#!/bin/bash
# This script generates the "student-notebooks" folder with student versions of
# the workshops in the "notebooks" folder. It also updates the TOC and keyword
# index based on the workshops in the "notebooks" folder.
# Make sure you have already installed nbgrader
# (https://nbgrader.readthedocs.io/en/stable/user_guide/installation.html)
# and nbpages (https://pypi.org/project/nbpages/).

# Update TOC and indexes
nbpages


# Re-creating student-notebooks folder
rm -r student-notebooks
nbgrader quickstart student-notebooks


# Copying notebooks in instructor's folder to the new source folder in student-notebooks folder
for i in ./notebooks/*.ipynb
do
   s=${i##*/}
   fname=${s%.ipynb}
   mkdir ./student-notebooks/source/$fname
   cp $i ./student-notebooks/source/$fname/$fname.ipynb
done


# Create assignments in release folder
cd student-notebooks
for i in ./source/*
do
   nbgrader db assignment add ${i##*/}
   nbgrader assign ${i##*/}
done


# Delete source folder
rm -r source


# Re-format student-notebooks folder and delete release folder
for i in ./release/*
do
   s=${i##*/}
   fname=${s%.ipynb}
   #echo $fname
   chmod 777 $i/*
   cp $i/* ./$fname.ipynb
done
rm -r release


# Copy over the Media and other folders to student-notebooks folder
cp -r ../notebooks/Media ./Media
cp -r ../notebooks/expected_outputs ./expected_outputs
cp -r ../notebooks/outputs ./outputs
cp -r ../notebooks/inputs ./inputs


# Edit TOC and index so that links are to the student versions
sed 's/\/notebooks\//\/student-notebooks\//g' toc.ipynb > _toc.ipynb
sed 's/\/notebooks\//\/student-notebooks\//g' index.ipynb > _index.ipynb

# Remove old toc file and index file
rm toc.ipynb
rm index.ipynb
