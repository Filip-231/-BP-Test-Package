"""Command line interface for BP Test Package."""
from typing import Optional

import click
from loguru import logger

from bptestpackage import utils, workflows


@click.group()
@click.pass_context
def show(_: click.Context) -> None:
    """Cli sub command."""


@show.command()
@click.option("-p", "--partition", nargs=1, help="Specifies partition column.")
@click.option(
    "-m",
    "--mode",
    type=click.Choice([update_mode.value for update_mode in utils.Mode]),
    required=True,
    help="Specifies mode.",
)
@click.option("-c", "--column", "columns", multiple=True, help="Specifies columns.")
@click.option(
    "--prod-env",
    is_flag=True,
    default=False,
    help="Boolean flag which indicates the Prod/Dev Environments. ",
)
@click.pass_context
def arguments(
    context: click.Context,
    partition: tuple[str, str],
    mode: Optional[str],
    columns: tuple[str, ...],
    prod_env: bool,
) -> None:
    """Execute bp-test-package workflow."""
    assert context.parent
    assert context.parent.parent
    workflow = workflows.Workflow()
    if prod_env:
        logger.info("Production environment.")
    workflow.print_arguments(
        context.parent.parent.params["name"],
        context.parent.parent.params["version"],
        partition,
        mode,  # type: ignore
        columns,
    )
