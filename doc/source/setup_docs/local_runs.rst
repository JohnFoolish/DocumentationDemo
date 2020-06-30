####################################
Recreating this Repo's Documentation 
####################################

In order to generate a local copy of the html documentaiton that is 
present in this repo, first you need to clone this repo by going to 
the project's `GitHub Page <https://github.com/JohnFoolish/testDemo>`_.

Once you've done this, be sure to install the requirements listed in 
the *requirements.txt* file. You can do this by running ::

    pip install -r requirements.txt
	
from the command line. This will ensure you have all of the required 
python modules that the demos and python scripts depend on. 

After you have done this, you can follow the steps mentioned in  
:doc:`sphinx_intro` to build the html files with either the Makefile
or sphinx-build methods. 