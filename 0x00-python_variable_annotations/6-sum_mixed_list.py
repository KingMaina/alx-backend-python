#!/usr/bin/env python3

"""Contains a type annoted function, sum_mixed_list,
    that return the sum of a list made of ints and floats
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Returns the sum of a list of a mix of floats and integers

        Parameters
        ----------
        mxd_lst (List[int | float]): A list of floats and integers

        Returns
        -------
        (float): The sum of the float and integer values in the list
    """
    sum: float = 0.0
    for value in mxd_lst:
        sum += value
    return sum
