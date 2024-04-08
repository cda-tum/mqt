"""Nox sessions."""

from __future__ import annotations

import argparse

import nox

nox.needs_version = ">=2024.3.2"
nox.options.default_venv_backend = "uv|virtualenv"


@nox.session(reuse_venv=True)
def docs(session: nox.Session) -> None:
    """
    Build the docs. Use "--non-interactive" to avoid serving. Pass "-b linkcheck" to check links.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("-b", dest="builder", default="html", help="Build target (default: html)")
    args, posargs = parser.parse_known_args(session.posargs)

    serve = args.builder == "html" and session.interactive
    extra_installs = ["sphinx-autobuild"] if serve else []
    session.install("-r", "docs/requirements.txt", *extra_installs)
    session.chdir("docs")

    if args.builder == "linkcheck":
        session.run("sphinx-build", "-b", "linkcheck", ".", "_build/linkcheck", *posargs)
        return

    shared_args = (
        "-n",  # nitpicky mode
        "-T",  # full tracebacks
        f"-b={args.builder}",
        ".",
        f"_build/{args.builder}",
        *posargs,
    )

    if serve:
        session.run("sphinx-autobuild", *shared_args)
    else:
        session.run("sphinx-build", "--keep-going", *shared_args)
