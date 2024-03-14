#!/usr/bin/env python3

"""Contains a type annoted function,that performs a zoom operation
"""
from typing import List, Tuple


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """Zoom

        Parameters
        ----------
        lst (List): A list of values to zoom
        factor (float): Factor to zoom by

        Returns
        -------
        (tuple): Tuple
    """
    zoomed_in: List[int] = [
        item for item in lst
        for _ in range(int(factor))
    ]
    return zoomed_in

array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
