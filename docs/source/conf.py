import sphinx_rtd_theme
import os
import sys
# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'GroupCalculator'
copyright = '2025, Tim Schütte, Felix Brandt'
author = 'Tim Schütte, Felix Brandt'
release = '0.0.1'

sys.path.insert(0, os.path.abspath('../../GroupCalculator'))  # Pfad zum übergeordneten Verzeichnis

html_theme = "sphinx_rtd_theme"
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',  # Docstrings automatisch einbinden
    'sphinx.ext.viewcode',  # Quellcode-Links hinzufügen
    'sphinx.ext.napoleon',  # Google- und NumPy-Docstring-Format unterstützen
]

templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']
