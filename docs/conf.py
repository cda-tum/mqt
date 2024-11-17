"""Sphinx configuration file."""

from __future__ import annotations

from typing import TYPE_CHECKING

import pybtex.plugin
from pybtex.style.formatting.unsrt import Style as UnsrtStyle
from pybtex.style.template import field, href

if TYPE_CHECKING:
    from pybtex.database import Entry
    from pybtex.richtext import HRef

project = 'mqt'
author = 'Chair for Design Automation, Technical University of Munich'
version = '1.0'
release = '1.0.0'
language = "en"
project_copyright = "2023, Chair for Design Automation, Technical University of Munich"

master_doc = "index"

templates_path = ["_templates"]

extensions = [
    "myst_nb",
    "sphinx.ext.intersphinx",
    "sphinxcontrib.bibtex",
    "sphinxcontrib.cairosvgconverter",
    "sphinx_design",
    "sphinx_copybutton",
    "sphinxext.opengraph",
]

source_suffix = [".rst", ".md"]

exclude_patterns = [
    "_build",
    "**.ipynb_checkpoints",
    "**.jupyter_cache",
    "**jupyter_execute",
    "Thumbs.db",
    ".DS_Store",
    ".env",
    ".venv",
]

pygments_style = "colorful"

add_module_names = False

numfig = True
numfig_secnum_depth = 0

modindex_common_prefix = ["mqt."]

intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
    "qiskit": ("https://docs.quantum.ibm.com/api/qiskit/", None),
    "core": ("https://mqt.readthedocs.io/projects/core/en/latest/", None),
    "ddsim": ("https://mqt.readthedocs.io/projects/ddsim/en/latest/", None),
    "qmap": ("https://mqt.readthedocs.io/projects/qmap/en/latest/", None),
    "qcec": ("https://mqt.readthedocs.io/projects/qcec/en/latest/", None),
    "qecc": ("https://mqt.readthedocs.io/projects/qecc/en/latest/", None),
    "bench": ("https://mqt.readthedocs.io/projects/bench/en/latest/", None),
    "predictor": ("https://mqt.readthedocs.io/projects/predictor/en/latest/", None),
    "qudits": ("https://mqt.readthedocs.io/projects/qudits/en/latest/", None),
    "qubomaker": ("https://mqt.readthedocs.io/projects/qubomaker/en/latest/", None),
    "syrec": ("https://mqt.readthedocs.io/projects/syrec/en/latest/", None),
}
intersphinx_disabled_reftypes = ["*"]

myst_enable_extensions = [
    "amsmath",
    "colon_fence",
    "substitution",
    "deflist",
    "dollarmath",
]
myst_heading_anchors = 3

# -- Options for {MyST}NB ----------------------------------------------------

nb_execution_mode = "cache"
nb_mime_priority_overrides = [
    # builder name, mime type, priority
    ("latex", "image/svg+xml", 15),
]


# -- Options for references --------------------------------------------------
class CDAStyle(UnsrtStyle):
    """Custom style for including PDF links."""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.abbreviate_names = True

    def format_url(self, _e: Entry) -> HRef:  # noqa: PLR6301
        """Format URL field as a link to the PDF."""
        url = field("url", raw=True)
        return href()[url, "[PDF]"]


pybtex.plugin.register_plugin("pybtex.style.formatting", "cda_style", CDAStyle)

bibtex_bibfiles = ["lit_header.bib", "refs.bib"]
bibtex_default_style = "cda_style"

copybutton_prompt_text = r"(?:\(\.?venv\) )?(?:\[.*\] )?\$ "
copybutton_prompt_is_regexp = True
copybutton_line_continuation_character = "\\"

# -- Options for LaTeX output ------------------------------------------------

sd_fontawesome_latex = True
image_converter_args=["-density", "300"]
latex_engine = "pdflatex"
latex_documents = [
    (
        master_doc,
        "mqt_handbook.tex",
        r"The MQT Handbook\\{\Large A Summary of Design Automation Tools and\\ Software for Quantum Computing}",
        r"""Chair for Design Automation\\ Technical University of Munich, Germany\\\href{mailto:quantum.cda@xcit.tum.de}{quantum.cda@xcit.tum.de}""",
        "howto",
        False),
]
latex_logo = "_static/mqt_dark.png"
latex_elements = {
    "papersize": "letterpaper",
    "releasename": "Version",
    "printindex": r"\footnotesize\raggedright\printindex",
    "tableofcontents": "",
    "sphinxsetup": "iconpackage=fontawesome",
    "extrapackages": r"\usepackage{qrcode,graphicx,calc,amsthm,etoolbox,flushend}",
    "preamble": r"""
\patchcmd{\thebibliography}{\addcontentsline{toc}{section}{\refname}}{}{}{}
\newtheorem{example}{Example}
\def\subparagraph{} % because IEEE classes don't define this, but titlesec assumes it's present
    """,
    "extraclassoptions": r"conference,onecolumn",
    "fvset": r"\fvset{fontsize=\small}",
    "figure_align": "htb",
}
latex_domain_indices = False
latex_docclass = {
    "howto": "IEEEtran",
}

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
