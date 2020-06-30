########################################
Best Practices with Sphinx Documentation
########################################

This section will be discussing how to properly ensure that all of 
your code is properly documented, and how to take advantage of all
of Sphinx's powerful tools to create fantastic documentation for it. 
(If you think that this documentation looks fantastic, read on! 
Otherwise ... I don't think that this will be much help)

Setting up the Python file
##########################
First and foremost, in order to document your python scripts, you 
need to ensure that your scripts are properly formatted. There are
two main ways that you can ensure this.

1) Since Sphinx is written using python, it first has to import your
scripts before generating the autodocs for them. Because of this, if
you have parts of your script that are outside of a ::
    
	if __name__ == '__main__':
	    #your code here
	
block, they will run when generating your sphinx documentation. This
can cause a lot of problems, since you don't want to run your 
code every time you try to build the documentation. 

2) Sphinx's autodocs tools will grab out any comments surrounded by 
triple quotes and interpret them as restructured text. Due to this,
you can include a triple quote comment block at the beginning of your
script, and it will be displayed by the autodocs tools before showing 
any of the functions/classes/methods documented. Do not write 
anything in the ::
    
	"""
	comment
	"""
	
format that you do not want included inside of your documentation. 

Docstrings/Doctests with Sphinx
###############################

Setting up the Docstrings/Doctests
----------------------------------
The most powerful part of using Sphinx comes from their autodoc 
generation. For EMADE, we concluded that the best practice would be 
to use `Google docstrings <https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example\_google.html>`_
to document our python scripts. Inside of these docstrings, you can 
also use pycharm to generate doctests. By including a ' >>> ' inside
the docstring, you can run tests from within the docstrings in the
following manner: ::

    def add(x, y):
	""" A simple function to add two numbers together.
	
	This function is designed purely as a demonstration for the
	doctest formatting. The first use of >>> is where you can give 
	the function with a set of parameters, and the second use of >>>
	should contain the expected result. By adding the sphinx 
	extension *sphinx.ext.doctest* in the **conf.py** file, you can
	also add doctests into the restructured text itself. 
	
	>>> add(5, 4)
	>>> 9
	
	Args:
	    x (int): The first number
		y (int): The second number
		
	Returns:
        int: The result of adding x and y together

    """		
	
Using Sphinx's napoleon extension, it will automatically generate 
the documentation in restructured text format from the Google 
docstring. (This also is the case for Numpy docstrings)

You can see an example of the restructured text output at the bottom
of :doc:`../intro`.

Integrating the Documentation 
-----------------------------
In order to generate the autodocs using Sphinx, you first must make
sure you have set the path to your source directory properly inside 
of **conf.py**. After that, you can very easily reference the code 
by adding the following to your restructured text document ::

    .. automodule:: [name of python file]
	   :[options]:
	
	
An important note is that you should just put the name of the python 
file without the **.py** extension there. There are many different 
options that can be included underneath automodule. You can include
``:members:`` to include all functions/methods that do not start with
"_". If you want to include those private functions as well, you can 
add in the option ```:undoc-members:```. You can find more options on
the official `Sphinx autodoc documentation <https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html#module-sphinx.ext.autodoc>`_.
	
Alternatively, you can generate restructured text files that will 
automatically include all private, public, and inherited functions or
methods by running 

    .. code-block:: bash
	
	sphinx-apidoc -o [output] [source]
	
This will loop over all python files in the source directory and put 
their restructured text version in the output directory. More 
information can be seen here: `Sphinx Apidoc <https://www.sphinx-doc.org/en/master/man/sphinx-apidoc.html>`_.	

Putting it all Together
#######################
Well, now we've discussed how to properly prepare the python
scripts for documentation and how to integrate the documentation into
restructured text documents. The next step is in actually generating 
the html documentation from the restructured text. First, make sure 
that all of your files are listed in toctrees. If they are not, then
you will not be easily able to visit those files. Think of them as 
nodes that haven't been connected to the rest of the restructured 
text tree. Once you have made sure your restructured text structure
is how you want it, go back to your command line of choice. 

The Makefile Method
-------------------
To generate the html, you can go to the directory where Sphinx 
created the Makefile. From there, run ::

    make html 
	
in order to generate the html file. They will be automatically 
saved inside of *build/html* if you chose separate build and source
directories at Sphinx startup.  

The Sphinx-build method
-----------------------
Alternatively, you can go to the directory where Sphinx created 
the **conf.py** file and run ::

 	sphinx-build [source directory] [output directory]

This will take the **conf.py** file located in the source directory, 
then output the html file inside of the output directory. 

Sidenote: Jupyter Notebooks
===========================
For a quick sidenote, you can also use Sphinx to generate html files 
for Jupyter Notebook tutorials, complete with inline matplotlib plots
and line numbers. In order to do this, you need to also create a 
'requirements.txt' file in the root directory of your project. This 
text file should be in the following format: ::

    # -*- coding: utf-8 -*-
	[required module 1]
	[required module 2]
	etc.
	
Where the required modules are the names of any dependencies that the
Jupyter Notebooks require to run. You should also include the 
extension *nbsphinx* in order to get the Jupyter Notebook to 
display. See the following link for more examples: 
`<https://nbsphinx.readthedocs.io/en/0.7.1/>`_
 


Conclusions
###########
Now you should be able to generate a local build of your 
documentation straight from the python source code. There are many 
more ways to beef up the documentation with fancy extensions or 
website styles. If you want to read a more in depth tutorial which
teaches the basics of getting set up with Sphinx as well as how to 
get into more advanced topics, read through the tutorial created by
the matplotlib team `here <https://matplotlib.org/sampledoc/index.html>`_.

If you want to learn how to host your documentation online with a 
hosting service such as `Readthedocs <https://readthedocs.org/>`_ or
 `Netlify <https://matplotlib.org/sampledoc/index.html>`_ , then read
on. 



	
