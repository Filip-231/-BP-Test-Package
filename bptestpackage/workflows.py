"""Workflow module for BP Test Package."""

from loguru import logger


class CustomError(Exception):
    """Exception raised when some custom error happen."""


class Workflow:
    """Workflow class for cli."""

    def __init__(self) -> None:
        """Initialize dWorkflow class."""

    @staticmethod
    def print_arguments(*args: tuple) -> None:
        """Prints every cli argument."""
        logger.info(f"Arguments: {args}.")
