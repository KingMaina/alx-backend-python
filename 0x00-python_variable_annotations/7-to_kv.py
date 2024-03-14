#!/usr/bin/env python3

"""Contains a type annoted function, to_kv,
    that returns a tuple made of a string
    and the square of a float or integer
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Returns a tuple made of a string and the square
        of an integer or float

        Parameters
        ----------
        k (str): A string
        v (Union[int | float]): An integer or float value

        Returns
        -------
        (float): A tuple made up of a string and
            the square of the integer/float, v
    """
    return (k, v**2)
