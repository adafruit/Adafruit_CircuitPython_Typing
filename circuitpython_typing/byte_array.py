# SPDX-FileCopyrightText: Copyright (c) 2024 Nate Gay
# SPDX-License-Identifier: MIT
"""
`circuitpython_typing.byte_array`
================================================================================

Type annotation definitions for device drivers. Used for non-volatile memory access.

* Author(s): Nate Gay
"""


from typing import overload, Union

from typing_extensions import Protocol

from . import ReadableBuffer


class ByteArray(Protocol):
    """Protocol for ByteArray used for NVM access."""

    def __bool__(self) -> bool:
        ...

    def __len__(self) -> int:
        """Return the length. This is used by (len)"""

    @overload
    def __getitem__(self, index: slice) -> bytearray:
        ...

    @overload
    def __getitem__(self, index: int) -> int:
        ...

    def __getitem__(self, index: Union[slice, int]) -> Union[bytearray, int]:
        """Returns the value at the given index."""

    @overload
    def __setitem__(self, index: slice, value: ReadableBuffer) -> None:
        ...

    @overload
    def __setitem__(self, index: int, value: int) -> None:
        ...

    def __setitem__(
        self, index: Union[slice, int], value: Union[ReadableBuffer, int]
    ) -> None:
        """Set the value at the given index."""
