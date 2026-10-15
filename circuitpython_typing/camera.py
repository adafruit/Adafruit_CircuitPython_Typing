# SPDX-FileCopyrightText: Copyright (c) 2026 Scott Shawcroft for Adafruit Industries
#
# SPDX-License-Identifier: MIT

"""
`circuitpython_typing.camera`
================================================================================

Type annotation definitions for camera sensor drivers. Used by `mipicsi`.

* Author(s): Scott Shawcroft
"""

from typing import TYPE_CHECKING

from typing_extensions import Protocol

if TYPE_CHECKING:
    import mipicsi


class CameraSensor(Protocol):
    """Protocol for a camera sensor driver compatible with `mipicsi.Camera`.

    A sensor driver provides these properties and methods. The
    `mipicsi.Camera` object reads the properties to configure the MIPI
    CSI-2 receiver for the sensor's current mode, and calls ``_start``
    and ``_stop`` itself as streams start and stop; user code should
    not call them. See the sensor properties documentation for what
    each value should describe.

    ``CameraSensor`` drivers include `sc2336.SC2336`.
    """

    @property
    def width(self) -> int:
        """The width of the frames the sensor transmits, in pixels."""

    @property
    def height(self) -> int:
        """The height of the frames the sensor transmits, in pixels."""

    @property
    def pixel_format(self) -> "mipicsi.PixelFormat":
        """The `mipicsi.PixelFormat` of the frames the sensor transmits."""

    @property
    def lane_bit_rate_mbps(self) -> int:
        """The MIPI data lane bit rate, in Mbps."""

    @property
    def data_lanes(self) -> int:
        """The number of MIPI data lanes the sensor transmits on."""

    @property
    def bayer_order(self) -> "mipicsi.BayerOrder":
        """The `mipicsi.BayerOrder` of the sensor's RAW output."""

    def _start(self) -> None:
        """Take the sensor out of standby so it streams frames.
        Internal: the `mipicsi.Camera` receiver calls it automatically
        when a `videocore.VideoBuffer` starts playing the camera.
        """

    def _stop(self) -> None:
        """Put the sensor into standby so it stops streaming.
        Internal: the `mipicsi.Camera` receiver calls it automatically
        when playback stops.
        """