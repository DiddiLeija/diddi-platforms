# Sphinx config file.

# we want some extensions, so we are including them here:
extensions = [
    # first-party
    "sphinx.ext.autodoc",
    "sphinx.ext.todo",
    "sphinx.ext.extlinks",
    "sphinx.ext.intersphinx",
    # third-party
    "sphinx_copybutton",
]

language = "en"
project = "Diddi Platforms"
author = "Diego Ramirez"
copyright = "2023-present, Diego Ramirez"

# version = pkg_version
# release = version

# HTML specs
html_theme = "furo"
