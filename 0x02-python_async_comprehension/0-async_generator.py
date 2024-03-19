#!/usr/bin/env python3

"""Contains a coroutine that loops 10 times while yielding
random numbers"""
import random
import asyncio
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """Loops 10 times and yields a random number in [0..10]

        In each loop, the generator waits for 1 second then
        yields a random number between 0 and 10

        Parameters
        ----------
        None

        Yields
        ------
        Random number between 0 and 10
    """
    for _ in range(11):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
