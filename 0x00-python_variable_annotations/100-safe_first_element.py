#!/usr/bin/env python3

"""Contains a type annoted function, safe_first_element, that
    returns the first element of the argument or None
"""
from typing import Sequence, Any, Optional


def safe_first_element(lst: Sequence[Any]) -> Optional[Any]:
    """Returns the first element of the argument or None

        Parameters
        ----------
        lst (Sequence[Any]): Any subscriptable value

        Returns
        -------
        (Union[Any, None]): The first element of lst or None
    """
    if lst:
        return lst[0]
    else:
        return None
