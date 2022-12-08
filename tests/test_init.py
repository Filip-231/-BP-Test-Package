"""Unit tests for data feed init interface."""
from unittest.mock import Mock

import click
import pytest
import pytest_mock
from click.testing import CliRunner

import bptestpackage


@pytest.mark.parametrize(
    "optional_parameter",
    ["--prod-env", None],
)
def test_dft_define_feed(
    workflow_mock: Mock,
    runner: CliRunner,
    mocker: pytest_mock.MockerFixture,
    optional_parameter: str,
) -> None:
    """Assert bppackage(...) command invokes with subcommands show parameters.

    :param workflow_mock: Workflow mock
    :param runner: Cli runner for testing purposes
    :param mocker: MockerFixture used to patch objects
    :param optional_parameter: Optional date column parameter
    """
    path = "docs/"
    mocker.patch.object(click.types.Path, "convert", return_value=path)
    parameters = [
        "--name",
        "name",
        "--version",
        "1234567890",
        "--path",
        "docs/",
        "show",
        "arguments",
        "--partition",
        "column",
        "--mode",
        "START",
        "--column",
        "A",
        "--column",
        "B",
    ]
    if optional_parameter:
        parameters.append(optional_parameter)
    workflow_mock.return_value.print_arguments.return_value = None

    result = runner.invoke(bptestpackage.bppackage, parameters)
    assert result.exit_code == 0
