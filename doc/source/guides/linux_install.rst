EMADE Installation on Linux
===========================

Requirements
------------

EMADE requires Python v3.4+ EMADE requires the following Python
Libraries - numpy - pandas - sklearn - tensorflow - keras - deap - scipy
- psutil - lxml - matplotlib - opencv (cv2) - hmmlearn - PyWavelets -
multiprocess - sqlalchemy

Instructions
------------

1.  Install `Git <https://git-scm.com/>`__ > Git is a tool to deal and
    manage repositories in GitHub. The EMADE source files are located in
    a GitHub repository, therefore we’ll need a tool to easily download
    it (i.e. clone the repository)

    -  For Ubuntu/Debian, ``sudo apt-get install git``. For other Linux
       distributions, click
       `here <https://git-scm.com/download/linux>`__

2.  Install `GIT LFS <https://git-lfs.github.com/>`__. Official
    instructions can be found
    `here <https://help.github.com/articles/installing-git-large-file-storage/>`__
    >\ *We will be downloading about ~5GB of files. Since GitHub doesn’t
    allow one to have such big repositories. Therefore, we need Git LFS
    in order to download large repositories*

    -  Navigate to https://git-lfs.github.com/ and click **Download**
    -  On your computer, unzip the downloaded file anywhere you like
    -  Open Terminal
    -  Change to working directory to the folder to which you unzipped
       the files with ``$ cd ~/Downloads/git-lfs-1.X.X``
    -  Install it by running the command ``$ sudo ./install.sh``
    -  Verify the installation was successful with
       ``$ git lfs install``, which should yield you
       ``Git LFS initialized``

3.  (Optional) Run the command below in order to reduce username and
    password prompts ``$ git config --global credential.helper cache``
4.  Clone the `git
    repository <https://github.gatech.edu/emade/emade/>`__ at your
    /home/ directory > Now we will clone (i.e. download) the repository

    -  Run ``$ git clone https://github.gatech.edu/emade/emade``
    -  You will need to enter your GT Username and GT Password

5.  Install `Anaconda 3 <https://www.anaconda.com/>`__ >\ *Anaconda is
    an open source distribution of Python and R programming languages
    for large-scale data processing, predictive analytics, and
    scientific computing*

    -  Download the .sh file
       `here <https://www.anaconda.com/download/>`__, and click on
       **Download** for Python 3.\* version
    -  Change your working directory to where you downloaded the file
       with ``$ cd ~/Downloads``
    -  Make sure that the file is executable with
       ``$ chmod +x Anaconda3-*.sh``
    -  Make sure to type ``yes`` when it asks if you would like the
       ‘installer to prepend the Anaconda3 install location to PATH’
    -  Close the current Terminal and open a new one in order to change
       the default python version.
    -  **Note:** *As of 2018-03-20, when trying to run
       ``$ anaconda-navigator``, it will not be able to run, and you
       will have to downgrade pip to the version 9.0.1 with
       ``$ pip install pip==9.0.1``* > By this point, you should have
       your Home folder as [Step 6]({{
       “/assets/images/linux_instructions/step6.png” \| absolute_url }})

6.  Change to the EMADE directory with ``$ cd emade``
7.  Install `OpenCV <https://opencv.org/>`__ with
    ``$ conda install opencv`` > This is a super nice library that is
    widely used for computer vision applications
8.  Install `Hidden Markov Models for Python
    (hmmlearn) <https://github.com/hmmlearn/hmmlearn>`__ with
    ``$ pip install hmmlearn`` > This is a library that is used to
    develop Hidden Markov Models
9.  Install `TensorFlow <https://www.tensorflow.org/>`__ with
    ``$ pip install tensorflow`` or with ``$ conda install tensorflow``
    > TensorFlow is an open-source library for numerical computation
    using data flow graphs. The graph nodes represent mathematical
    operations, while the graph edges represent the multidimensional
    data arrays (tensors) that flow between them. This flexible
    architecture lets you deploy computation to one or more CPUs or GPUs
    in a desktop, server, or mobile device without rewriting code.
10. Install `Keras <https://keras.io/>`__, a high-level neural networks
    API, with ``$ pip install keras`` or with ``$ conda install keras``
    > This is an API used to develop neural networks in a high-level.
11. Now you should be almost set! At this point, you will be on the Git
    Branch *``python3_conve``*. This is not the branch we’re looking
    for. The one we want to work with is the *``Image``* branch. So
    change the branch it with ``$ git checkout Image``
12. Build all of the required files with ``$ bash reinstall.sh``
13. Install `MySQL <https://www.mysql.com/>`__ with
    ``$ sudo apt-get update`` and
    ``$ sudo apt-get install mysql-server``. After the installation is
    complete, the ``mysql_secure_installation`` utility will run,
    prompting you to define the mysql root password. [Step12]({{
    “/assets/images/linux_instructions/step12.png” \| absolute_url }})
