This is an introduction to the Fellow's documentation!
============================================

Here you can find a list of the current packages I have written for
this project. They all include numpy docstrings!

Here are some helpful pointers regarding the creation of the autodocs:

* You need to have the extension `sphinx.ext.autodocs` added to the conf.py

* You also need to add  `.. automodule:: [module_name]`
 to the rst file you wantto add the script's documentation to.

* Important note: the autodocs automatically goes loads any string comment
(`"""[comment]"""`) with restructured text when writing the documentation.

* Also, any script being documented need to include a `if __name__ == '__main__'`


Current modules!
----------------

.. toctree::
   :maxdepth: 1
   :caption: Contents:

   sphinx_intro
   basic_code
   

.. automodule:: basic_code
   :members:
