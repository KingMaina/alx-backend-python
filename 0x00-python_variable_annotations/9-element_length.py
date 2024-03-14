#!/usr/bin/env python3

"""Contains a type annoted function, make_multiplier,
    that takes a float, multiplier, and returns a function that
    multiplies a float by the multiplier
"""
from typing import Tuple, List, Sequence, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Takes an iterable and returns a tuple that has the element and
        its length

        Parameters
        ----------
        lst (Iterable[Sequence]): Iterable i.e list

        Returns
        -------
        (List[Tuple[Sequence, int]]): List of tuples
    """
    return [(i, len(i)) for i in lst]
