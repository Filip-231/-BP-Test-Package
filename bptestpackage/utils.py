"""This is utils module for BP Test Package."""
import enum


def test_method(value: int) -> int:
    """This is test method two

    :param value: Example number.
    """
    return value * value


class Mode(enum.Enum):
    """Mode enum."""

    START = "START"
    END = "END"
    PROGRESS = "PROGRESS"
