========================
Slidoc
========================

Use Python, Pypandoc, and Pandoc to create HTML slides from source files.

Package Organization
--------------------

::

    slidoc
    ├── README.rst           <- The top-level README that describes this project
    │
    ├── docs                 <- A default Sphinx project; see sphinx-doc.org for details
    │   ├── Makefile         <- An automation file for GNU Make
    │   ├── conf.py          <- The main Sphinx configuration file
    │   ├── index.rst        <- The main reStructuredText file that lists all source files
    │   ├── readme.rst       <- A reStructuredText file to include the README in the docs
    │   ├── modules.rst      <- A reStructuredText file that lists all modules
    │   ├── slidoc.rst       <- A reStructuredText file to include the slidoc module in the docs
    │   ├── test_slidoc.rst  <- A reStructuredText file to include the test_slidoc module in the docs
    │   └── tests.rst        <- A reStructuredText file that lists all test files
    │
    └── src                  <- Source code for use in this project
        └── slidoc
            ├── __init__.py  <- Makes Slidoc a Python package
            └── slidoc.py    <- Contains module code

Project based on the `Cookiecutter Data Science project template <https://drivendata.github.io/cookiecutter-data-science>`__.
