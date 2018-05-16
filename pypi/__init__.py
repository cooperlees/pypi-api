#!/usr/bin/env python3

from typing import NamedTuple, Optional


class __version_info__(NamedTuple):
    major: int
    minor: int
    micro: int
    releaselevel: Optional[int]
    serial: Optional[str]


v = __version_info__(major=0, minor=0, micro=1, releaselevel=None, serial=None)
__version__ = f"{v.major}.{v.minor}.{v.micro}"
