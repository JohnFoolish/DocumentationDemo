####################
How to set up Sphinx
####################
This restructured text file documents how to properly set up a 
set of sphinx documentation for use in the future. Setting up 
documentation like this isn't as hard as you might think.

Downloading Sphinx
##################
In order to create documentation similar to this, you first need to 
go ahead and download sphinx using pip or conda by running from 
the command line: 

    .. code-block:: bash
	
        conda install -c conda-forge sphinx
	
or:
    .. code-block:: bash
	
        pip install sphinx
	
Once you have done this, you can go ahead and start setting up your 
project's file strucure.

Formatting Sphinx's File Structure
##################################
The way that this demonstration was created was by putting a separate 
directory called *doc* inside the main git repository. This directory
is at the same level as the *src* directory, which is where the 
majority of the source code is located. 

Once you have navigated to where you want to store your documentation 
you should run from the command line:: 
    .. code-block:: bash
	
        sphinx-quickstart
		
inside that directory. This will generate a few different files which
will be discussed below. Choose to have separate source and build 
directories.

conf.py
*******
This is the main configuration file for the sphinx documentation 
build. You will need to uncomment the ::

        import os
	import sys
	sys.path.insert(0, os.path.abspath('.'))
	
lines, and also go ahead and add the directory where your python 
files are located to the system path like so ::
    sys.path.append(os.path.abspath('[path]')
	
where [path] is the path to reach the directory your python files 
are located from the directory **conf.py** is located in. 

In order to display the autodocs and load both google and numpy 
docstrings as restructured text, make sure your extension list looks
like the following: ::
    extensions = ['sphinx.ext.autodoc', 'sphinx.ext.napoleon']
	
if you download other sphinx extensions, be sure to link the path to 
the folder that they are stored in using the same format discussed 
above. Downloading third party extensions are essential when 
interfacing sphinx with matplotlib or jupyter notebook.	

You can think of the **conf.py** file as a the main configuration and
setup file. Each of the variables you set here are used to determine
how the sphinx build is configured. 

If you want a specific file excluded from the sphinx build, include 
the filepath inside of the *exclude_patterns* list.

In order to get the documentation to build on readthedocs and also 
netlify, we need to add a variable *master_doc* set equal to 'index'.
This notifies the sphinx builder what it should treat as the main 
page for the documentation website. 

Below is an image of the current setup of **conf.py** for the
*william* branch of the documentation demo:

.. image:: ../_static/config.JPG
   :align: center 
	

.. topic:: IMPORTANT: 

    Both readthedocs and netlify use a linux machine to compile sphinx,
    so in order to ensure you can build the documentation on a local 
    windows machine, we added the following code: ::
        import platform
    	if platform.system() == "Windows":
	    sys.path.append(os.path.abspath('..\..\src'))
	else:
            sys.path.append(os.path.abspath('../../src'))
		
		
index.rst
*********
This is the main page of the documentation. This serves as the first
page that people see when going to your documentation's website. The
toctree is the table of contents, and the maxdepth signifies how many 
titles/sections of each listed file to show. 

When adding files to the table of contents, you do not need to 
include their file name extensions. You also must use the "/" to mark
separate directories instead of the Windows way of "\\".


