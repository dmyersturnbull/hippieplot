"""
Command-line interface for ${project|.
"""

from __future__ import annotations

import logging

import typer

from hippieplot import __title__, __version__, __copyright__, metadata

logger = logging.getLogger(__package__)
cli = typer.Typer()


class Commands:
    """Collection of commands for hippieplot."""

    @classmethod
    def info(cls, verbose: bool = False) -> None:
        """
        Get info about hippieplot.
        Args:
            verbose: Print extended information.
        """
        typer.echo("{} version {}, {}".format(__title__, __version__, __copyright__))
        if verbose:
            typer.echo(str(metadata.__dict__))


if __name__ == "__main__":
    cli()


__all__ = [Commands]