#!/usr/bin/env python3
"""Measure average execution time for the wait_n coroutine."""

import asyncio
import time
from importlib import import_module
from typing import Union

# Dynamically import wait_n from 1-concurrent_coroutines
module = import_module("1-concurrent_coroutines")
wait_n = module.wait_n

def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the total execution time for wait_n(n, max_delay) and returns
    the average time per coroutine.
    """
    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    end = time.time()
    total_time = end - start
    return total_time / n
