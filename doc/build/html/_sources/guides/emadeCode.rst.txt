.. _guide_to_emade_code_structure:

Guide to EMADE Code Structure
=============================

.. _about_this_guide:

About this Guide
----------------

This wiki entry is to help you understand the flow of EMADE source code
and how you can modify it yourself! In addition to this wiki, files are
also commented according to Sphinx autodoc'ing standards, which you
should follow if you add or change code. If you're looking to run your
first optimization problem with emade, check out the :ref:`guide_to_xml_EMADE_input` or the `GitHub readme`_.

.. _xml_input:

XML Input
---------

The problem definition for any GP in EMADE is input as an XML file.
Example XML files are located in the templates folder. Information
defined in the XML file includes the objectives, datasets, functions for
mutation, crossover, and evaluation, as well as connection information
for the SQL database.

didLaunch.py
------------

The file run from the command line is didLaunch.py. Reading through this
file will help you understand the command-line arguments passed into
EMADE. If a previous database is provided, it is loaded from the pickle
file. If not, the problem definition is read from an XML file.

database_tree_evaluator.py
--------------------------

This file is used for debugging a specific individual. It pulls the
individual from the database and reruns its evaluation so that you can
see any errors that occur.

data.py
-------

Methods to read in data from standard formats are in data.py (e.g. .csv,
.gzip, .jpeg, .gz). The file is provided in the XML and the type of file
is deduced from the file ending within data.py. This file also
implements the data types used in the main loop, GTMOEPDataInstance and
GTMOEPDataPair.

There are unit tests in /src/UnitTests/data_unit_test_v3.py for this
file.

gp_framework_helper.py
----------------------

This file adds all primitives and terminals to the main evolutionary
loop/DEAP toolkit. If you want to implement your own terminal or
primitive, you will need to associate it here.

launchGTMOEP.py
---------------

This file parses the XML configuration file. These configurations are
saved into three python dictionaries to be later passed to a master
subprocess that will run the main evolutionary loop and worker
subprocesses that will evaluate individuals. These dictionaries are also
saved as a binary data file with the pickle library with a name
determined by the original process id bound to the launchGTMOEP.py
process. This file can be thought of as the preprocessing for
didLaunch.py, which is the main driver script for both the master and
worker processes.

gtMOEP.py
---------

This file contains the main evolutionary loop for both the master and
workers. The current non-dominated front, current-generation
individuals, and statistics are saved into the database file here as the
master algorithm progresses, and can be examined directly with a
database client such as sqlite3. Individuals are passed between the
master and workers through the database, and each instance of gtMOEP.py
runs as a separate process so that resource manageme

.. _GitHub readme: https://github.gatech.edu/emade/emade