.. _guide_to_debugging_individual_algorithms:

Guide to Debugging Individual Algorithms
========================================

When you first create a random population of individuals (i.e.
algorithms), many are likely to die. You can see why they have died in
the error_string column of the individuals database table. For example,
if there is not the possibility of outputting the correct datatype,
EMADE will automatically kill that individual to speed up overall
evaluation time, and will display that "The primitives cannot
categorically convert from input of desired type to desired type of
output."

As EMADE progresses beyond its first generation, only the algorithms
that return finite values on all objectives will be propagated forward
to be chosen for mutation or crossover; this should lead to a normal and
productive evolutionary run. But what happens if an algorithm that you
think should execute correctly returns all NULL objective values? Or,
worse yet, all of your algorithms return NULL values? Well, then it is
time to debug using the following technique(s).

.. _evaluating_individual_algorithms:

Evaluating Individual Algorithms
--------------------------------

Because string representations of algorithms are stored as pickled
objectives in the individuals table of the database, you can actually
unpickle them yourself to run them on a local instance of EMADE. The
database_tree_evaluator.py file takes the path to an XML and an
individual's hash from the DB as command-line arguments to set up a
gtMOEP instance and the appropriate function pointers to run your
individual for you. The database connection information is read from the
XML, **but make sure to set use/reuse according to your intention.**

.. _seeding_your_own_algorithms:

Seeding Your Own Algorithms
---------------------------

Sometimes the initial algorithms are simply not apt for solving complex
problems. You can introduce candidate algorithms by simply typing them
as string representations of a valid individual, and using the
seeding_from_file.py file. The text file with your individuals is
new-line delineated, and will not accept individuals that are already
present in the database.

For example, to start the process of classifying stream data, you may
wish to feed the output of an FFT into a machine learner. Example
seeding code is included in the SeedingFiles of the main directory.

The syntax is:

``python seeding_from_file.py templates/input_file.xml seeding_test_1``

.. _common_reasons_why_algorithms_fail:

Common Reasons Why Algorithms Fail
----------------------------------

If all of your algorithms fail, it is most likely the result of
malformed data, XML input, or an incorrectly installed instance of
EMADE. If you wish to debug individuals, here is a list of common
error_strings.

libcuda.so not found: this individual tried to use tensorflow or keras
on an installation that expects a GPU, but there is no GPU available.

``Found array with 0 feature(s)...``