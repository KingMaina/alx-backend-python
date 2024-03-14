#!/usr/bin/env python3

"""Contains a type annoted function,that safely retrieces a value
"""
from typing import Any, Optional, Mapping, TypeVar, Union

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None]) -> Union[Any, T]:
    """Retrieves a value from a dictionary

        Parameters
        ----------
        dct (Mapping): A dictionary
        key (Any): string representing key in the dictionary
        default(Optional[T]): Default value to return

        Returns
        -------
        (Optional[T]): Key value or the default value
    """
    if key in dct:
        return dct[key]
    else:
        return default
