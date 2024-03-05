# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'simple_math'
copyright = '2024, Flavio Ferella'
author = 'Flavio Ferella'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']
import sys
import os
sys.path.insert(0,os.path.abspath('/mnt/c/Users/flafe228/Desktop/all_documents/phd/courses/Advance_Python_Programming/Exercises/day4/'))

extensions = [
 'sphinx.ext.autodoc',
 'numpydoc'
]