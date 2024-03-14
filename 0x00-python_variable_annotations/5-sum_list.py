#!/usr/bin/env python3

"""Contains a type annoted function, sum_list,
    that return the sum of a list of float
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """Returns the sum of a list of floats

        Parameters
        ----------
        input_list (List[float]): A list of float values

        Returns
        -------
        (float): The sum of the float values in input_list
    """
    sum: float = 0.0
    for value in input_list:
        sum += value
    return sum
