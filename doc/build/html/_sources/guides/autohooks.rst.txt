Git Hooks
=========

Overview
--------

The ``hooks`` directory of this project contains an implementation of a Python-based, multi-platform `Git hook`_ manager based on `Autohook`_. This allows for developers to run code before and after issuing Git commands to improve workflow and ensure consistency.

Requirements
------------

-  Python >= 3.5
-  yapf to use ``run_yapf.py`` script

Installation
------------

Run ``install_hooks.bat`` or ``install_hooks.sh`` depending on your
system to install the Git hooks.

Usage
-----

By running the install scripts, the hook manager will be installed into
the Git hook location at ``.git/hooks``, causing them to automatically
be run when the corresponding Git commands are executed. This project
can be integrated into any Git repository by copying the install scripts
and the ``hooks`` directory.

To add a new Git hook, place the script in ``hooks/scripts``, and place
the command to run in a file which is named as the appropriate
client-side hook. For example, to add a script ``check_code.py`` as a
pre-commit hook, add it to the ``hooks/scripts`` directory, and add
``python check_code.py`` to the file ``hooks/pre-commit.txt``. To add a
script ``log_commit.sh`` as a post-commit hook, add it to the scripts
directory, and add ``bash check_code.py`` to the file
``hooks/post-commit.txt``. Scripts will be run in the order that they
are listed.

Included Hook Scripts
---------------------

.. _check_docstringspy:

check_docstrings.py
~~~~~~~~~~~~~~~~~~~

This pre-commit hook checks Python files for missing docstrings. The
script checks "public" functions, classes, and class methods for missing
docstrings. Public in this context just means that it does not have an
underscore "_" at the beginning of the name. The ``BRANCH_REGEX``
variable controls which branches this script will run on. The default is
to run on all branches, but for example it may be changed to run on only
the master branch with ``re.compile("master")``. The ``STRICT`` variable
controls whether the script will reject the commit if any documentation
is missing, or just print a warning message.

.. _jira_commit_msgpy:

jira_commit_msg.py
~~~~~~~~~~~~~~~~~~

This prepare-commit-msg hook automatically adds Jira ids to commit
messages. The script will check whether the branch name has a valid Jira
id as a prefix, and will add it to the beginning of the commit message
if so. The ``JIRA_ID_REGEX`` variable controls the format which Jira ids
can take.

.. _run_yapfpy:

run_yapf.py
~~~~~~~~~~~

This pre-commit hook runs the Google code formatter `YAPF`_ on Python
files. The ``BRANCH_REGEX`` variable controls which branches this script
will run on. The default is to run on all branches, but for example it
may be changed to run on only the master branch with
``re.compile("master")``.

Supported Hook Types
--------------------

-  applypatch-msg
-  commit-msg
-  post-applypatch
-  post-checkout
-  post-commit
-  post-merge
-  post-receive
-  post-rewrite
-  post-update,
-  pre-applypatch
-  pre-auto-gc
-  pre-commit
-  pre-push
-  pre-rebase,
-  pre-receive
-  prepare-commit-msg
-  update

.. _Git hook: https://git-scm.com/book/en/v2/Customizing-Git-Git-Hooks
.. _Autohook: https://github.com/nkantar/Autohook
.. _YAPF: https://github.com/google/yapf