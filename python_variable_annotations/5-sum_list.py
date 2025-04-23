#!/usr/bin/env python3
"""Type-annotaded function - sum_list"""


from typing import List


def sum_list(input_list: List[float]) -> float:
    """Returns the sum of a list of floats"""
    return sum(input_list)  # sum() is a built-in function
