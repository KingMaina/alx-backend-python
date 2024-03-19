#!/usr/bin/env python3

"""Contains a coroutine that measures the runtime of executing
    `async_comprehension` 4 times in parallel
"""
import asyncio
import time
from typing import Awaitable

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Measures the runtime of execting `async_comprehension`
        4 times in parallel

        Parameters
        ----------
        None

        Returns
        -------
        Total runtime
    """
    startTime: float = time.perf_counter()

    # Execute 4 tasks in parallel
    await asyncio.gather(async_comprehension(),
                         async_comprehension(),
                         async_comprehension(),
                         async_comprehension())
    endTime: float = time.perf_counter()

    # Return total runtime
    return endTime - startTime
