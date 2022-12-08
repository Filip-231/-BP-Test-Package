"""ClI interface unit tests."""

from unittest import mock

import click
import pytest
from click import testing

from bptestpackage import cli


@pytest.mark.parametrize("optional_parameter", ["--prod-env", None])
@pytest.mark.parametrize(
    "mode_parameter",
    [
        {"mode": "START", "columns": ()},
        {"mode": "END", "columns": ()},
        {"mode": "PROGRESS", "columns": ("col1", "col2")},
    ],
)
def test_arguments_cli_command(
    runner: testing.CliRunner,
    bppackage_context: click.Context,
    workflow_mock: mock.NonCallableMagicMock,
    optional_parameter: str,
    mode_parameter: dict,
) -> None:
    """Assert print_parameters(...) command invokes with different set of parameters.

    :param runner: Cli runner for testing purposes
    :param bppackage_context: click.Context of main bppackage command
    :param workflow_mock: Workflow mock
    :param optional_parameter: Optional parameter
    :param mode_parameter: Dict with mode and columns parameters
    """
    partition = "column"
    mode = mode_parameter["mode"]
    columns = mode_parameter["columns"]
    parameters = ["--partition", partition, "--mode", mode]
    if columns:
        for column in columns:
            parameters.extend(["--column", column])
    if optional_parameter:
        parameters.append(optional_parameter)

    result = runner.invoke(cli.arguments, parameters, parent=bppackage_context)
    assert result.exit_code == 0
    assert bppackage_context.parent

    workflow_mock.print_arguments.assert_called_once_with(
        bppackage_context.parent.params["name"],
        bppackage_context.parent.params["version"],
        partition,
        mode,
        columns,
    )
