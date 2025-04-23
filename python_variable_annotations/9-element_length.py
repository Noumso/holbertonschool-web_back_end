#!/usr/bin/env python3
"""Return values with the types"""


from typing import Iterable, Sequence, Tuple, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """returns a list of tuples containing elements and their lengths"""
    return [(i, len(i)) for i in lst]
