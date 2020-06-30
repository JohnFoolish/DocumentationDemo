EMADE Installation on Mac
=========================

Requirements
------------

EMADE requires Python v3.4+ EMADE requires the following Python
Libraries - numpy - pandas - sklearn - tensorflow - keras - deap - scipy
- psutil - lxml - matplotlib - opencv (cv2) - hmmlearn - PyWavelets -
multiprocess - sqlalchemy

Instructions
------------

1. Install Homebrew

      *Homebrew is an installation package manager. It will make
      installing the rest of the packages extremely easy.*

   -  Open Terminal and run
      ``/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"``
      to install Homebrew

2. Install `Git <https://git-scm.com/>`__ > *Git is a tool to deal and
   manage repositories in GitHub. The EMADE source files are located in
   a GitHub repository, therefore we’ll need a tool to easily download
   it (i.e. clone the repository)*

   -  Open Terminal and run ``$ brew install git``

   -  Verify that it was installed correctly by running
      ``$ git --version`` and make sure it returns something similar to
      ``git version 2.9.3``

3. Install `GIT LFS <https://git-lfs.github.com/>`__. Official
   instructions can be found
   `here <https://help.github.com/articles/installing-git-large-file-storage/>`__
   >\ *We will be downloading about ~5GB of files. Since GitHub doesn’t
   allow one to have such big repositories. Therefore, we need Git LFS
   in order to download large repositories*

   -  Open Terminal
   -  Install it by running the command ``$ brew install git-lfs``
   -  Verify the installation was successful with ``$ git lfs install``,
      which should yield you ``Git LFS initialized``

4. (Optional) Run the commands below in order to reduce username and
   password prompts

   -  ``$ git config --global user.name "<your gt login username>"``
   -  ``$ git config --global user.email "<your gt login email>"``
   -  ``$ git config --global credential.helper cache``

5. Clone the `git repository <https://github.gatech.edu/emade/emade/>`__
   at your /home/ directory > Now we will clone (i.e. download) the
   repository. **Note** *This might take a few hours because of the
   large files size. It would be in your best interest to keep your
   computer plugged in to its charger, and possibly run this part
   overnight when you will not need to use it.*

   -  Run ``$ cd`` which will take you to the home directory
   -  Run ``$ git clone https://github.gatech.edu/emade/emade``
   -  You might need to enter your GT Username and GT Password. Your
      password may seem like nothing is being typed. Just type it in and
      hit enter, even if no characters show up as you type your
      password.

6. Install `Anaconda 3 <https://www.anaconda.com/>`__ >\ *Anaconda is an
   open source distribution of Python and R programming languages for
   large-scale data processing, predictive analytics, and scientific
   computing*

   -  Download the ``.pkg`` file
      `here <https://www.anaconda.com/download/>`__, and click on
      **Download** for Python 3.\* version
   -  Change your working directory to where you downloaded the file
      with ``$ cd ~/Downloads``
   -  Click on the downloaded ``.pkg`` file and follow the instructions
      to install Anaconda
   -  If asked, make sure to type ``yes`` when it asks if you would like
      the ‘installer to prepend the Anaconda3 install location to PATH’
   -  Close the current Terminal and open a new one in order to change
      the default python version.
   -  **Note:** *As of 2018-03-20, when trying to run
      ``$ anaconda-navigator``, it will not be able to run, and you will
      have to downgrade pip to the version 9.0.1 with
      ``$ pip install pip==9.0.1``*

      -  This shouldn’t affect most Mac machines, but if you receive
         such an error, try using this downgrade to fix it

   -  Go back to the home directory by running ``$ cd``

7. Change to the EMADE directory with ``$ cd emade``

8. Install `OpenCV <https://opencv.org/>`__ with
   ``$ conda install opencv`` > This is a super nice library that is
   widely used for computer vision applications

**NOTE** *For the rest of these instructions that use ``pip``, if you
receive an error relating to the python version, or asking you to use
``sudo`` in your command, try running the same command with ``pip3``
instead of ``pip``*

9.  Install `Hidden Markov Models for Python
    (hmmlearn) <https://github.com/hmmlearn/hmmlearn>`__ with
    ``$ pip install hmmlearn`` > This is a library that is used to
    develop Hidden Markov Models
10. Install `TensorFlow <https://www.tensorflow.org/>`__ with
    ``$ pip install tensorflow`` or with ``$ conda install tensorflow``
    > TensorFlow is an open-source library for numerical computation
    using data flow graphs. The graph nodes represent mathematical
    operations, while the graph edges represent the multidimensional
    data arrays (tensors) that flow between them. This flexible
    architecture lets you deploy computation to one or more CPUs or GPUs
    in a desktop, server, or mobile device without rewriting code.
11. Install `Keras <https://keras.io/>`__, a high-level neural networks
    API, with ``$ pip install keras`` or with ``$ conda install keras``
    > This is an API used to develop neural networks in a high-level.
12. For the remaining packages below, run ``pip install <package name>``
    to ensure you have all the relevant packages to run EMADE. Some may
    print out that you already have the requirement satisfied, which
    means you have already installed that package, and that is not an
    error.

    -  numpy
    -  pandas
    -  sklearn
    -  tensorflow
    -  keras
    -  deap
    -  scipy
    -  psutil
    -  lxml
    -  matplotlib
    -  opencv (cv2)
    -  hmmlearn
    -  PyWavelets
    -  multiprocess
    -  sqlalchemy

13. Now you should be almost set! At this point, you will be on the Git
    Branch *``master``* or *``python3_conve``*. This is not the branch
    we’re looking for. The one we want to work with is the *``Image``*
    branch.

    -  So change the branch it with ``$ git checkout Image``
    -  **NOTE** *This may take a while to complete, but not as long as
       cloning the repository*

14. Build all of the required files with ``$ bash reinstall.sh``
15. Install `MySQL <https://www.mysql.com/>`__ by following the
    instructions
    `here <https://dev.mysql.com/doc/refman/5.7/en/osx-installation-pkg.html>`__
    (**recommended**)

    -  or by running ``$ brew install mysql`` (**NOT Recommended** for
       MySQL).
    -  Make sure that you immediately set the root password if it asks
       for one. If it does not ask for one, then run
       ``mysqladmin -u root password '<yourpassword>'`` making sure to
       use single quotes ``'`` around what you want your root password
       to be.

       -  **NOTE** *Many users had trouble because they were unable to
          reset their root password, and the default password was
          unknown.*\ `Here <https://stackoverflow.com/a/22851247/4501263>`__\ *is
          a tutorial you can follow if you also experience that issue,
          to force reset your root password*
