#!/usr/bin/env python3
"""annotated function make_multiplier"""

from typing import Callable, Iterator, Union, Optional


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''make callable'''
    def make_mulitply(x: float) -> float:
        return (x * multiplier)
    return make_mulitply
