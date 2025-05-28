import os
import sys
sys.path.insert(0, os.path.abspath('.'))

project = 'Official Bridge Documentation'
copyright = '2024, SatoshiLabs'
author = 'SatoshiLabs'

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon',
    'myst_parser'
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
html_title = 'Official Bridge Documentation'
html_favicon = '_static/favicon.ico'

master_doc = 'index'