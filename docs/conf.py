# flake8: noqa

# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import sphinx_rtd_theme

project = "there"
copyright = "2022, 0x0elliot, SyedAhkam"
author = "0x0elliot, SyedAhkam"
release = "v0.1"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ["sphinxcontrib.redoc", "sphinx_rtd_theme"]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]

redoc = [
    {
        "name": "there API",
        "page": "api-doc",
        "spec": "schema.yml",
        "embed": True,
        "opts": {"suppress-warnings": True, "hide-hostname": True},
    }
]
redoc_uri = "https://unpkg.com/redoc@2.0.0-rc.66/bundles/redoc.standalone.js"
