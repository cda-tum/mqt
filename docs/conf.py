"""Sphinx configuration file."""

project = 'mqt'
author = 'Chair for Design Automation, Technical University of Munich'
version = '1.0'
release = '1.0.0'
language = "en"
project_copyright = "2023, Chair for Design Automation, Technical University of Munich"

master_doc = "index"

templates_path = ["_templates"]

extensions = [
    "myst_parser",
    "sphinx.ext.intersphinx",
    "sphinx_design",
    "sphinx_copybutton",
    "sphinxext.opengraph",
    "sphinx.ext.imgconverter",
]

source_suffix = [".rst", ".md"]

exclude_patterns = [
    "_build",
    "**.ipynb_checkpoints",
    "Thumbs.db",
    ".DS_Store",
    ".env",
    ".venv",
]

pygments_style = "colorful"

add_module_names = False

modindex_common_prefix = ["mqt."]

intersphinx_mapping = {
    # "python": ("https://docs.python.org/3", None),
    # "matplotlib": ("https://matplotlib.org/stable/", None),
    # "qiskit": ("https://qiskit.org/documentation/", None),
    "core": ("https://mqt.readthedocs.io/projects/core/en/latest/", None),
    "ddsim": ("https://mqt.readthedocs.io/projects/ddsim/en/latest/", None),
    "qmap": ("https://mqt.readthedocs.io/projects/qmap/en/latest/", None),
    "qcec": ("https://mqt.readthedocs.io/projects/qcec/en/latest/", None),
    "qecc": ("https://mqt.readthedocs.io/projects/qecc/en/latest/", None),
    "bench": ("https://mqt.readthedocs.io/projects/bench/en/latest/", None),
    "predictor": ("https://mqt.readthedocs.io/projects/predictor/en/latest/", None),
    "syrec": ("https://mqt.readthedocs.io/projects/syrec/en/latest/", None),
}
intersphinx_disabled_reftypes = ["*"]

myst_enable_extensions = [
    "colon_fence",
    "substitution",
    "deflist",
]
myst_heading_anchors = 3

copybutton_prompt_text = r"(?:\(venv\) )?(?:\[.*\] )?\$ "
copybutton_prompt_is_regexp = True
copybutton_line_continuation_character = "\\"

# -- Options for LaTeX output ------------------------------------------------

sd_fontawesome_latex = True
image_converter_args=["-density", "300"]

# -- Options for HTML output -------------------------------------------------
html_theme = "furo"
html_title = "The Munich Quantum Toolkit (MQT)"
html_static_path = ["_static"]
html_theme_options = {
    "light_logo": "mqt_dark.png",
    "dark_logo": "mqt_light.png",
    "source_repository": "https://github.com/cda-tum/mqt/",
    "source_branch": "main",
    "source_directory": "docs/",
    "navigation_with_keys": True,
    "sidebar_hide_name": True,
}
html_css_files = [
    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.1.1/css/all.min.css",
    "custom.css",
]
