.. _guide_to_using_gcp_cnn:

Guide to Using GCP-CNN
======================

.. _about_cgp_cnn:

About CGP-CNN
-------------

CGP-CNN is a tool that uses evolutionary techniques to optimize the
structure of a deep neural network for a given dataset (i.e. order of
the layers, types of layers, hyperparameters, preprocessing). The
process of designing an accurate deep neural network is often a lot of
trial and error or experience. With CGP-CNN, we aim to use Cartesian
Genetic Programming to efficiently explore the space of deep structures.
CGP-CNN is a separate program from EMADE, though it uses several of the
data structures and libraries of EMADE.

.. _how_to_get_started_with_cgp_cnn:

How to get started with CGP-CNN
-------------------------------

On this repository, each branch is for a different dataset. So far, we
have

#. mnist - a set of black and white hand drawn images of numbers 0-9:
   http://yann.lecun.com/exdb/mnist/
#. quickdraw - a set of black and white hand drawn images of animals,
   plants, and objects: https://quickdraw.withgoogle.com/data

First, make sure to read the README for technical details on setting up
your environment. To get started, choose a branch and run src/main.py
This will start the evolutionary process on the data set. On the command
prompt, you will be able to see a print of the mutated structures as
well as their accuracy as they are being trained. At the end of each
generation, the dominant individuals will be reevaluated and printed to
the screen for you to see. The evaluation log folder will also contain a
copy of the command prompt print. From its output, you will be able to
see the models that are on the pareto front

.. _how_it_works:

How it works
------------

We built this project in two steps.

#. Starting from EMADE, a Cartesian Genetic Programming framework was
   created as a sister to EMADE. You can check this out at the cgp
   branch of rtalebi3/emade.
#. Using this framework, we designed the program to specifically
   optimize deep networks.

To gain an understanding of how Cartesian Genetic Programming works and
how it is different from the GP that EMADE uses, please check out the
github wiki page pf rtalebi3/emade.
https://github.gatech.edu/rtalebi3/emade/wiki

In its implementation for deep neural networks, most of the code we
changed was in the fromGPFramework/methods_v4.py, individual.py,
operators_v2.py, and problem_v2.py

.. _defining_layers:

Defining layers
---------------

The primitives in the evolutionary process are the types of layers
possible and their hyperparameters. These are defined in methods_v4.py
as functions. Note, these functions all input a tensor and output a
tensor. Their hyperparameters are set by arguments that are passed to
them and also evolutionarily optimized. Also, layers are declared as
operators (and their arguments and inputs are specified) in the
operators_v2.py. To add a primitive, simply define the function in
methods_v4.py under its commented classification type, and declare it in
operators_v2.py. It will automatically be used in the evolution process.

Evaluation
----------

The networks are evaluated by training them for a set number of epochs
with a training subset of the dataset, and then evaluated on the
validation set. It is then assigned a fitness which is (1-accuracy, time
taken). You can change the objectives in problem_v2.py by adding a
metric and concatenating/replacing the fitness values. This works by
passing batches through self.x, which is a tensorflow placeholder object
that is used in the other functions throughout cgp-cnn as the input to
the model, and then training on self.y which is a placeholder for the
output of the deep neural network. The tensorflow graph (self.g),
self.x, and self.y are all part of the problem object, that is inherited
by individual.

Configuration
-------------

Instead of the XML that EMADE uses, CGP-CNN uses a configuration.py file
that contains global variables for the run. For example, batch size,
number of epochs, size of convolutional filters, etc. These are
basically hyperparemeters for the CGP-CNN run. They are often dependent
on the size and complexity of the dataset.

Dataset
-------

To change the dataset, follow the following steps.

#. Obtain the dataset and determine the size of the input data.
#. Update configuration.py with the correct data information.
#. Determine the objective function, and rewrite the getFitness function
   within problem.py.
#. Update the deepemade hyperparameters in configuration.py,this is done
   in lieu of updating an .xml file for normal emade.

FAQ
---

#. Does CGP-CNN work with GPU optimization?
	Yes. In the beginning of the run, CGP-CNN will output whether it has detected and is using GPU optimization.
#. How does CGP-CNN deal with very large networks?
	If the system runs out of a memory limit/time limit that is set in configuration.py, the individual is killed and assigned a bad fitness.
#. Can you save the dominant deep network structure after it is trained?
	Yes. But the code for this is in the armemade branch of emade under the CGPFramework, and hasn't yet been checked into the CGP-CNN repository.
