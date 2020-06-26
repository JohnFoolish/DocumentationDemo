Guide to XML Emade Input
========================

Emade accepts problem definitions via the XML input fed into
launchGTMOEP.py. To better understand how your problem definition is
parsed from the XML and ultimately fed into the main evolutionary loop,
consult the `Guide to EMADE Code Structure`_.

objectives
----------

Emade is capable of handling an arbitrary number of objectives, but all
of them must be minimization. The weight of the objective function must
therefore be negative, but it may be a decimal percentage. The
achievable and goal attributes affect selection, where individuals
behind the achievable point are not likely to be selected for crossover.
Lastly, the upper and lower tags are bounds for the calculation of
hypervolume.

pyConfig/gridEngineParameters
-----------------------------

These two sections provide the path to Python and other attributes for
server-side execution. launchGTMOEP.py creates a file in the main
directory called gridEngineJobSubmit_master_SOMEPROCESSID.sh. This is a
script to run your problem on a Unix server. If you are running Emade
locally, this file is unused.

dbConfig
--------

This section is used if you create a local MySQL database with Emade by
running the didLaunch.py file without a "-d" flag. If you are using a
pre-instantiated or remote database, this option is unused.

dataset
-------

This is where you provide both your test and training data. If you
provide k files for each within the montecarlo subsection, then Emade
will perform k-fold cross-validation. Note however that you must fold
the data yourself. You must also specify the type of your data, which
can be "featuredata", "streamdata", "filterdata", or "imagedata". These
labels determine how your data will be read in and fed to classifiers.

evaluation
----------

This section specifies the file that contains methods to evaluate
individual fitness.

evolutionParameters
-------------------

These are parameters that control the evolutionary loop.

.. _paretofitness_parentsadult_paretofrontadult:

paretoFitness / parentsAdult / paretoFrontAdult
-----------------------------------------------

These are used to define the output that Emade writes as .txt files.

.. _Guide to EMADE Code Structure: Guide_to_EMADE_Code_Structure