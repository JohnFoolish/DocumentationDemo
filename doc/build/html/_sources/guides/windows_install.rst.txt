EMADE Installation on Windows
=============================

Requirements
------------

EMADE requires Python v3.4+ EMADE requires the following Python
Libraries - numpy - pandas - sklearn - tensorflow - keras - deap - scipy
- psutil - lxml - matplotlib - opencv (cv2) - hmmlearn - PyWavelets -
multiprocess - sqlalchemy

Instructions
------------

1. Install Anaconda

    -  Installation link https://www.anaconda.com/download/#windows
    -  Choose the proper installer for your operating system
    -  conda-cheatsheet link
     https://conda.io/docs/_downloads/conda-cheatsheet.pdf

2. Install Git

    -  Installation link https://git-scm.com/download/win
    -  github-git-cheatsheet link
       https://services.github.com/on-demand/downloads/github-git-cheatsheet.pdf

3. Add Git to Environment Variables

    -  Right Click PC icon -> Select Properties
    -  Select Advanced System Settings -> Click Environment Variables
    -  Select the Path that has ``Anaconda3`` -> Click Edit
    -  Click New -> Paste ``C:\Program Files\Git\cmd`` -> Click OK

4. Open Command Window (cmd)

    -  Run ``git version`` to verify Git Installation
    -  Run ``conda create --name py35 python=3.5`` to create a new
       environemnt (env)
    -  Activate the new env by running ``activate py35``
    -  Use ``pip`` to install the required libraries referenced above (e.g.,
       ``pip install pywt``)
    -  Use ``conda install -cmenpo opencv3`` to install opencv
    -  Note: ``conda intall`` does not work with some libraries, better use
       ``pip``

5. Clone EMADE and checkout the Image branch

    -  Note: This step requires a minimium of three hours to complete
    -  Open cmd
    -  Run ``git clone https://github.gatech.edu/emade/emade``
    -  Run ``cd emade``
    -  Run ``git checkout Image``
    -  Run ``reinstall.sh``
