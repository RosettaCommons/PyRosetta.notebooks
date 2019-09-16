
# coding: utf-8

# <!--NOTEBOOK_HEADER-->
# *This notebook contains material from [PyRosetta](https://RosettaCommons.github.io/PyRosetta);
# content is available [on Github](https://github.com/RosettaCommons/PyRosetta.notebooks.git).*

# <!--NAVIGATION-->
# < [Introduction to PyRosetta](http://nbviewer.jupyter.org/github/RosettaCommons/PyRosetta.notebooks/blob/master/notebooks/02.00-Introduction-to-PyRosetta.ipynb) | [Contents](toc.ipynb) | [Index](index.ipynb) | [Working with Pose residues](http://nbviewer.jupyter.org/github/RosettaCommons/PyRosetta.notebooks/blob/master/notebooks/02.02-Working-with-Pose-Residues.ipynb) ><p><a href="https://colab.research.google.com/github/RosettaCommons/PyRosetta.notebooks/blob/master/notebooks/02.01-Pose-Basics.ipynb"><img align="left" src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open in Colab" title="Open in Google Colaboratory"></a>

# # Pose Basics
# Keywords: pose_from_pdb(), sequence(), cleanATOM, annotated_sequence()

# In this lab, we will get practice working with the `Pose` class in PyRosetta. We will load in a protein from a PDB files, use the `Pose` class to learn about the geometry of the protein, make changes to this geometry, and visualize the changes easily with `PyMOL` and PyRosetta's `PyMOLMover`. 
# 
# On the corresponding `Pose` lab found on the PyRosetta website, you will find various useful commands to interrogate poses; these may come in handy for the exercises.
# 
# **PyRosetta Installation:**
# The following two lines will load in the PyRosetta library and load in database files. If this does not work, please notify the professor or the TA.

# In[5]:


# Notebook setup
import sys
if 'google.colab' in sys.modules:
    get_ipython().system('pip install pyrosettacolabsetup')
    import pyrosettacolabsetup
    pyrosettacolabsetup.setup()
    print ("Notebook is set for PyRosetta use in Colab.  Have fun!")


# In[1]:


from pyrosetta import *
init()


# ## Loading in a PDB File ##

# We will spend some time today looking at the crystal structure for the protein **PafA** (PDB ID: 5tj3) using Pyrosetta and PyMOL. PafA is an alkaline phosphatase, which removes a phosphate group from a phosphate monoester. In this structure, a modified amino acid, phosphothreonine, is used to mimic the substrate in the active site. Let's load in this structure with PyRosetta (make sure that you have the PDB file located in your current directory):
# 
# `cd google_drive/My\ Drive/student-notebooks/
# pose = pose_from_pdb("5tj3.pdb")`

# In[2]:


### BEGIN SOLUTION
pose = pose_from_pdb("inputs/5tj3.pdb")
### END SOLUTION


# Use `pose.sequence()` to look at the protein's sequence:

# In[3]:


# print out the sequence of the pose
### BEGIN SOLUTION
pose.sequence()
### END SOLUTION


# Sometimes PDB files do not conform to standards and need to be cleaned to be loaded successfully with PyRosetta. One way to make sure the file is loaded successfully is to only include the ATOM lines from the PDB file. Alternatively, you could use the cleanATOM function in pyrosetta.toolbox to achieve the same: 

# In[3]:


from pyrosetta.toolbox import cleanATOM
cleanATOM("inputs/5tj3.pdb")


# This method will create a cleaned 5tj3.clean.pdb file for you. Lets load this into PyRosetta as well:

# In[5]:


pose_clean = pose_from_pdb("inputs/5tj3.clean.pdb")


# In our case, we could load in the PDB file for 5tj3 without cleaning it. In fact, we've lost some residues when cleaning the PDB file with cleanATOM. What is the difference in the `sequence` of the `pose_clean` now, compared to before?

# In[6]:


# print out the sequence of the pose_clean
### BEGIN SOLUTION
pose_clean.sequence()
### END SOLUTION


# With the function `annotated_sequence` below, we can start to see in more detail what the differences are. Note that non-canonical amino acids and hetatms are spelled out more explicitly now.

# In[7]:


pose.annotated_sequence()


# In[8]:


pose_clean.annotated_sequence()


# ### Exercise 1: Inspecting pose sequences
# 
# Visually inspect the sequences to find the difference(s) between the `pose_clean.sequence()` and `pose.sequence()`. Were residues removed? Which ones?

# ### Bonus Exercise 1: Identifying differences in sequences
# 
# (Optional) Write a program to automatically find the differences between these two sequences

# Because this PDB file was able to load into PyRosetta successfully without the cleanATOM method, we're going to stick with this slightly larger `pose` through the rest of this lab.

# <!--NAVIGATION-->
# < [Introduction to PyRosetta](http://nbviewer.jupyter.org/github/RosettaCommons/PyRosetta.notebooks/blob/master/notebooks/02.00-Introduction-to-PyRosetta.ipynb) | [Contents](toc.ipynb) | [Index](index.ipynb) | [Working with Pose residues](http://nbviewer.jupyter.org/github/RosettaCommons/PyRosetta.notebooks/blob/master/notebooks/02.02-Working-with-Pose-Residues.ipynb) ><p><a href="https://colab.research.google.com/github/RosettaCommons/PyRosetta.notebooks/blob/master/notebooks/02.01-Pose-Basics.ipynb"><img align="left" src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open in Colab" title="Open in Google Colaboratory"></a>
