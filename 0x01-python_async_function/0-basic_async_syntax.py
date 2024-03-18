#!/usr/bin/env python3

"""Module containing a coroutine that waits for a random delay
    then returns the delay count
"""
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """ A coroutine that waits for a random delay between 0
        and max_delay, inclusive, then returns it

        Parameters
        ----------
        max_delay (float): The maximum delay the coroutine executes

        Returns
        -------
        float: The random delay that was chosen
    """
    random_delay: float = random.uniform(0, max_delay)
    await asyncio.sleep(random_delay)
    return random_delay
