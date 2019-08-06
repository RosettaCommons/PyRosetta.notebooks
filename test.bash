# Edit TOC and index so that links are to the student versions
sed 's/\/notebooks\//\/student-notebooks\//g' toc.ipynb > _toc.ipynb
sed 's/\/notebooks\//\/student-notebooks\//g' index.ipynb > _index.ipynb

# Remove old toc file and index file
rm toc.ipynb
rm index.ipynb

