#!/usr/bin/env python3

"""Contains a coroutine that collects 10 random numbers
    from `async_generator` using async comprehension"""
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Collects 10 random numbers from `async_generator`

        Parameters
        ----------
        None

        Returns
        -------
        List of 10 random numbers generated
    """
    return [i async for i in async_generator()]
