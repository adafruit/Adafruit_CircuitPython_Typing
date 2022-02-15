# SPDX-FileCopyrightText: Copyright (c) 2022 Dan Halbert for Adafruit Industries
#
# SPDX-License-Identifier: MIT
"""
`circuitpython_typing`
================================================================================

Types needed for type annotation that are not in `typing`


* Author(s): Alec Delaney, Dan Halbert
"""

__version__ = "0.0.0-auto.0"
__repo__ = "https://github.com/adafruit/Adafruit_CircuitPython_Typing.git"

from typing import Union
from array import array

ReadableBuffer = Union[bytes, bytearray, memoryview, array]
"""Classes that implement the readable buffer protocol
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
