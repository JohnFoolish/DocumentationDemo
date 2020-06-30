Pandoc
======

Overview
--------

`Pandoc`_ is a universal document converter which supports converting to and from lightweight markup formats, HTML formats, TeX formats, Wiki markup, and other document formats. 

Installation
------------

Follow the `installation instructions`_ on the Pandoc website to install on your system.

Usage with Sphinx
------------------

Pandoc can be used to convert various document formats to reStructuredText for use with Sphinx. For example, to convert a GitHub markdown formatted file into rst run the command

.. code-block:: bash

    pandoc README.md -f markdown_github -t rst -o README.rst

To convert a `MediaWiki markup`_ formatted file (e.g. from the `VIP wiki`_) into rst run the command

.. code-block:: bash

    pandoc common_emade_errors.txt -f mediawiki -t rst -o common_emade_errors.rst

Tips
----

* pandoc is not perfect. Many files will have to be manually tweaked after conversion to ensure that they render properly
* Try to ensure that each file has a main title in the source language, e.g. `# Title` in markdown
* In many cases, pandoc will create links in reStructuredText by defining the link at the bottom of the page, rather than directly at the location of the link. For example::

    Look at this `link to a page`_.
    .. _link to a page: https://www.google.com/

.. _Pandoc: https://pandoc.org/
.. _installation instructions: https://pandoc.org/installing.html
.. _MediaWiki markup: https://www.mediawiki.org/wiki/Help:Formatting
.. _VIP wiki: https://vip.gatech.edu/wiki/index.php/Automated_Algorithm_Design