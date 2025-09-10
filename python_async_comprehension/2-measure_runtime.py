#!/usr/bin/env python3
"""
Module 2-measure_runtime
Contains the coroutine measure_runtime that executes async_comprehension
four times in parallel using asyncio.gather(*...) and returns the total runtime.
"""

import asyncio
import time
from typing import Union

async_comprehension = __import__('1-async_comprehension').async_comprehension

async def measure_runtime() -> float:
    """
    Executes async_comprehension four times in parallel using asyncio.gather(*...)
    and returns the total runtime in seconds.
    """
    start_time = time.perf_counter()
    await asyncio.gather(*[async_comprehension() for _ in range(4)])
    end_time = time.perf_counter()
    return end_time - start_time
