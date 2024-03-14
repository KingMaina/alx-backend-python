#!/usr/bin/env python3

"""Contains a type annoted function, make_multiplier,
    that takes a float, multiplier, and returns a function that
    multiplies a float by the multiplier
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Takes a multipler calue and returns a functoin that
        mutliplies it with other float arguments

        Parameters
        ----------
        multiplier (float): Multiplier value

        Returns
        -------
        (Callable[[float], float]): Function that takes a
            float and multiplies it by the multipler
    """
    return lambda float_number: multiplier * float_number
