#!/usr/bin/env python3

"""Contains a type annoted function, floor,
    that returns the floor of a float argument
"""
import math


def floor(n: float) -> int:
    """Returns the floor of n

        Parameters
        ----------
        n (float): Float number

        Returns
        -------
        (int): The floor of n
    """
    return math.floor(n)
