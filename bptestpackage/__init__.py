"""Define the CLI interface for BP Test Package."""

import click

from bptestpackage import cli, validators


@click.group()
@click.option("-n", "--name", type=str, help="Specifies name.")
@click.option(
    "-v", "--version", type=validators.version_type, help="Specifies version."
)
@click.option(
    "-p",
    "--path",
    type=click.Path(exists=True, file_okay=True, dir_okay=True),
    help="Path which need to exist.",
)
@click.pass_context
def bppackage(_: click.Context, name: str, version: str, path: str) -> None:
    """
    Prints arguments.

    Example invocation:
    bppackage --name "name" --version 1234567890 --path "docs/" show arguments --partition "column" --mode "START" \
        --column "A" --column "B" --prod-env
    """
    if not path and not (name and version):
        raise click.exceptions.MissingParameter(
            "--name and --version has to be provided when --path is not used.",
        )


bppackage.add_command(cli.show)
