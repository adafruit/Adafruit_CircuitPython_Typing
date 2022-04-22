# SPDX-FileCopyrightText: Copyright (c) 2022 Alec Delaney
#
# SPDX-License-Identifier: MIT

"""
`circuitpython_typing.pil`
================================================================================

Type annotation definitions for PIL Images.

* Author(s): Alec Delaney
"""

from typing import Tuple

# Protocol was introduced in Python 3.8.
try:
    from typing import Protocol
except ImportError:
    from typing_extensions import Protocol


class PixelAccess(Protocol):
    """Type annotation for PIL's PixelAccess class"""

    # pylint: disable=invalid-name
    def __getitem__(self, xy: Tuple[int, int]) -> int:
        """Get pixels by x, y coordinate"""
        ...


class Image(Protocol):
    """Type annotation for PIL's Image class"""

    @property
    def mode(self) -> str:
        """The mode of the image"""
        ...

    @property
    def size(self) -> Tuple[int, int]:
        """The size of the image"""
        ...

    def load(self) -> PixelAccess:
        """Load the image for quick pixel access"""
        ...
