import os
import sys
# for autodoc
sys.path.insert(0, os.path.abspath(".."))

project = 'astrotraders'
copyright = '2023, kiriharu'
author = 'kiriharu'
release = '1.0.0'
extensions = ["sphinx.ext.autodoc"]
templates_path = ['_templates']
exclude_patterns = []
html_theme = 'furo'
html_static_path = ['_static']
