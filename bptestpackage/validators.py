"""Define the validators for  BP Test Package."""
from typing import Optional

import click


class VersionType(click.ParamType):
    """Return a custom Version type Click parameter."""

    name = "Version"

    def convert(
        self, value: str, param: Optional[click.Parameter], ctx: Optional[click.Context]
    ) -> Optional[str]:
        """Create a Version object from the value, failing if it is not a 10 digit numeric string.

        :param value: the value to convert
        :param param: the parameter that the value relates to
        :param ctx: context passed from click
        """
        if not len(value) == 10 or not value.isdigit():
            self.fail(
                f"{value!r} is not a valid version identifier - must be a 14 digit number",
                param,
                ctx,
            )
        return value


version_type = VersionType()
