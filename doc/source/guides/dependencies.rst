.. _guide_to_installing_dependencies:

Guide to Installing Dependencies
================================

.. _introduction_to_git_version_control_system_and_faq:

Introduction to Git Version Control System and FAQ
--------------------------------------------------

`Simple Introductory Guide to Git, with graphical illustrations and
installation <http://rogerdudler.github.io/git-guide/>`__

.. _git_large_file_system:

Git Large File System
---------------------

After following the introduction to Git installation and basic commands,
it is also recommended to install git-lfs to handle EMADE installation.

Windows
-------

Follow the manual installation on the `Git
website. <https://git-lfs.github.com/>`__

Mac
---

Install either Homebrew or MacPorts package manager for MacOS. Either
one is sufficient for EMADE and related Python packages.

`Installing Homebrew
(recommended) <https://www.howtogeek.com/211541/homebrew-for-os-x-easily-installs-desktop-apps-and-terminal-utilities/>`__

`Installing MacPorts <https://www.macports.org/install.php>`__

Then, install Git Large File System (LFS) by running the following
commands in Terminal (sudo may be required):

Homebrew: ``brew install git-lfs``

MacPorts: ``port install git-lfs``

Linux
-----

For Debian distributions (particularly Ubuntu 16.04), run the following:

.. code-block:: bash

	curl -s https://packagecloud.io/install/repositories/github/git-lfs/script.deb.sh | sudo bash
	sudo apt-get install git-lfs

`Source <https://askubuntu.com/questions/799341/how-to-install-git-lfs-on-ubuntu-16-04>`__

.. _recommended_package_versions:

Recommended Package Versions
----------------------------

While other versions may work, to be consistent with EMADE and the first
semester projects, it is recommended to install these software versions.

Generally, use Anaconda's virtual environment if possible. Otherwise,
use pip and your preferred package manager.

For Windows users, the GUI installers are recommended.

**NOTE: The minor versions (e.g. 3.5.xx) generally do not matter.**

+------------------+---------+---------------------------------------+
| Name             | Version | Notes                                 |
+==================+=========+=======================================+
| Python           | 3.5.0   | Very important, later versions may    |
|                  |         | not work with Scikit-learn or         |
|                  |         | Tensorflow                            |
+------------------+---------+---------------------------------------+
| Anaconda         | 4.5     | Very important. Will be installing    |
|                  |         | most packages in Conda.               |
+------------------+---------+---------------------------------------+
| Scikit-learn     | 0.19    | Later versions do not include         |
|                  |         | necessary packages                    |
+------------------+---------+---------------------------------------+
| Jupyter Notebook | 4.4.0   | Later Version should not cause any    |
|                  |         | difficulties. `Official installation  |
|                  |         | guide <https://jupyter.read           |
|                  |         | thedocs.io/en/latest/install.html>`__ |
+------------------+---------+---------------------------------------+
| Numpy            | 1.15    |                                       |
+------------------+---------+---------------------------------------+
| Matplotlib       | 3.1     | Use 2.1 if issues arise. Used for     |
|                  |         | visualizing pareto fronts graphs      |
+------------------+---------+---------------------------------------+
| Pandas           | 0.23    | Contains good input parsing functions |
|                  |         | (read_csv)                            |
+------------------+---------+---------------------------------------+
| Deap             | 1.2.2   | If you get a message saying that the  |
|                  |         | package cannot be found, try adding   |
|                  |         | the *conda-forge* channel to your     |
|                  |         | list of channels with this            |
|                  |         | command: ``conda c                    |
|                  |         | onfig --append channels conda-forge`` |
+------------------+---------+---------------------------------------+
| PyGraphViz       | 1.5     | Also used to visualize graphs         |
+------------------+---------+---------------------------------------+
| MySQL            | 8.0.12  | For MacOS: If suffering from remote   |
|                  |         | access difficulties, please refer to  |
|                  |         | `here <https://stac                   |
|                  |         | koverflow.com/questions/24729077/how- |
|                  |         | to-enable-remote-access-from-mac-osx- |
|                  |         | to-mysql-server-on-windows-server>`__ |
|                  |         | and                                   |
|                  |         | `here <https://dba.stackexchange.c    |
|                  |         | om/questions/55958/cant-remote-access |
|                  |         | -mysql-server-running-on-mac-os-x>`__ |
+------------------+---------+---------------------------------------+
| MariaDB          | 10.1.37 | Alternative to MySQL                  |
+------------------+---------+---------------------------------------+
| TensorFlow       | 1.12.0  |                                       |
+------------------+---------+---------------------------------------+

The above list may not be a complete list of all necessary packages. If
you encounter any new difficulties, please share!
