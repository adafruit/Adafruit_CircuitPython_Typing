# SPDX-FileCopyrightText: Copyright (c) 2022 Dan Halbert for Adafruit Industries
#
# SPDX-License-Identifier: MIT
"""
`circuitpython_typing`
================================================================================

Types needed for type annotation that are not in `typing`


* Author(s): Alec Delaney, Dan Halbert, Randy Hudson
"""

__version__ = "0.0.0-auto.0"
__repo__ = "https://github.com/adafruit/Adafruit_CircuitPython_Typing.git"


from typing import Union, Optional

# Protocol was introduced in Python 3.8.
try:
    from typing import Protocol
except ImportError:
    from typing_extensions import Protocol

from array import array

ReadableBuffer = Union[bytes, bytearray, memoryview, array]
"""Classes that implement the readable buffer protocol
  * `str`
  * `bytes`
  * `bytearray`
  * `memoryview`
  * `array.array`
"""

WriteableBuffer = Union[bytearray, memoryview, array]
"""Classes that implement the writeable buffer protocol
  * `bytearray`
  * `memoryview`
  * `array.array`
"""


class ByteStream(Protocol):
    """Protocol for basic I/O operations on a byte stream.
    Classes which implement this protocol include
    * `io.BytesIO`
    * `io.FileIO` (for a file open in binary mode)
    * `busio.UART`
    * `usb_cdc.Serial`
    """

    # Should be `, /)`, but not available in Python 3.7.
    def read(self, count: Optional[int] = None) -> Optional[bytes]:
        """Read ``count`` bytes from the stream.
        If ``count`` bytes are not immediately available,
        or if the parameter is not specified in the call,
        the outcome is implementation-dependent.
        """
        ...

    # Should be `, /)`, but not available in Python 3.7.
    def write(self, buf: ReadableBuffer) -> Optional[int]:
        """Write the bytes in ``buf`` to the stream."""
        ...
