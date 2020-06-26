.. _common_emade_errors:

Common Emade Errors
===================

.. _ssl_connection_error:

SSL Connection Error
--------------------

If you are on your own machine or install a non-global install of ssh,
you may be able to disable SSL Completely depending on your database
configuration. Otherwise, some success has been met by forcing the
PyMySQL driver by changing connection URLs to read
“mysql+pymysql://DBIP”. However, pymysql may be causing timeouts, and
should be tested on other setups.

.. _raise_ioerror_not_a_gzipped_file:

raise IOError, 'Not a gzipped file'
-----------------------------------

**Description:**
  Typically this occurs when a user tries running emade or a unit test for emade for the first time. The file being referred to is not a .gz file.
**Cause:**
  The normal cause of this error is that git-lfs was not properly installed/configured. This means that cloning emade pulled the pointers to all .gz files instead of the actual files.
**Solution:**
  1. Install git-lfs (Add Instructions here soon)
  2. In a command prompt, cd to the emade directory
  3. Run "git fetch origin --all"
  4. Run "git merge/rebase" (run git merge if you wish to keep any edits you have made, otherwise run git rebase)

.. _from_numpy.lib.arraypad_import__validate_lengths_importerror_cannot_import_name__validate_lengths:

from numpy.lib.arraypad import \_validate_lengths ImportError: cannot import name '_validate_lengths'
-----------------------------------------------------------------------------------------------------

**Description:**
  Typically happens when and older version of scikit-image is installed.
**Cause:**
  Emade requires scikit-image 0.14.2
**Solution:**
  Make sure scikit-image 0.14.2 is installed

  1. If you already have scikit-image installed with pip, run ``pip uninstall scikit-image``
  2. Run ``conda insall scikit-image-0.14.2``

.. _errno_8_nodename_nor_servname_provided_or_not_known:

[Errno 8] nodename nor servname provided, or not known
------------------------------------------------------

**Description:**
  Occurs on newer MacOS
**Cause:**
  Computer name is not recognized as localhost
**Solution:**
  Look at your /etc/hosts file and see if your host name is there
  
  1. Find your computer name (can be done using scoop.gethostname()
  2. sudo vim /etc/hosts and insert 127.0.0.1