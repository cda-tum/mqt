"""Nox sessions."""

from __future__ import annotations

from typing import TYPE_CHECKING

import nox

if TYPE_CHECKING:
    from nox.sessions import Session


@nox.session(reuse_venv=True)
def docs(session: Session) -> None:
    """Build the documentation.

    Simply execute `nox -s docs` to locally build and serve the docs.
    """
    session.install("-r", "docs/requirements.txt")
    session.chdir("docs")
    session.run("sphinx-autobuild", "-b", "html", ".", "_build/html")
