#!/usr/bin/env python3
"""
Module 2-measure_runtime
Contains coroutine measure_runtime that executes async_comprehension
in parallel using asyncio.gather(*...) and returns the runtime.
"""

import asyncio
import time
from typing import Union

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Executes async_comprehensionin parallel using asyncio.gather(*...)
    and returns runtime in seconds.
    """
    start_time = time.perf_counter()
    await asyncio.gather(*[async_comprehension() for _ in range(4)])
    end_time = time.perf_counter()
    return end_time - start_time
