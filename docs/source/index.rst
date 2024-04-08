.. sphinx-doc-test documentation master file, created by
   sphinx-quickstart on Wed Apr  3 13:27:06 2024.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to this documentation example!
========================================

There is basically nothing here I just want to try it with zero consequences :)
This is some **bold text**. This is some *italicized text*. Here's a `link <https://google.com/>`_.

.. Note::

  And finally, this is a note. This note could tell us something like the project is under development.


Note also that this theme is not built in and must be installed using the following command:

.. code-block::

     $ pip install sphinx-wagtail-theme
     $ pip install sphinx-rtd-theme

And then updating the conf.py file to include:

.. code-block::

     extensions.append("sphinx_wagtail_theme")
     html_theme = 'sphinx_wagtail_theme'

This documentation currently contains no automation but can be updated manually at any time using the following convenience commands

.. code-block::

     $ cd docs
     $ make html


For further information on customization, code description, automation, etc, see the `sphinx documentation <https://www.sphinx-doc.org/en/master/index.html>`_


Contents
--------

.. toctree::
   :maxdepth: 2

   usage
   examples
   legal


Additional resources
--------------------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
