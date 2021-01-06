"""
Command-line interface for hippieplot.
"""

from __future__ import annotations

import logging

import typer

logger = logging.getLogger(__package__)


cli = typer.Typer()


if __name__ == "__main__":
    cli()
