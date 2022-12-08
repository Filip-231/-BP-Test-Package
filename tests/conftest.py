"""Fixtures for tests."""

from unittest import mock

import click
import pytest
import pytest_mock
from click import testing


@pytest.fixture(name="runner")
def fixture_runner() -> testing.CliRunner:
    """Runner fixture for testing."""
    return testing.CliRunner()


@pytest.fixture(name="bppackage_context")
def fixture_bppackage_context() -> click.Context:
    """Dft main command context for testing purposes."""
    ctx = click.Context(click.Command("show"))
    ctx.parent = click.Context(click.Command("bppackage"))
    ctx.parent.params = {"name": "name", "version": "1234567890"}
    return ctx


@pytest.fixture(name="workflow_mock")
def get_workflow_mock(mocker: pytest_mock.MockerFixture) -> mock.NonCallableMagicMock:
    """Get mock of Workflow class.

    :param mocker: MockerFixture used to patch Workflow object
    """
    workflow = mocker.patch(
        "bptestpackage.workflows.Workflow", autospec=True
    ).return_value
    workflow.project = "test_project"
    return workflow
