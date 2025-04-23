#!/usr/bin/env python3
"""Type-annotaded function - floor"""

import math


def floor(n: float) -> int:
    """Returns the floor of the float"""
    floornum = math.floor(n)
    return int(floornum)
