#!/usr/bin/env python3
"""Concurrent coroutines example: wait_n coroutine using wait_random."""

import asyncio
import importlib
from typing import List

# Dynamically import the previous file
module = importlib.import_module("0-basic_async_syntax")
wait_random = module.wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """wait_random n times with max_delay and return delays in order"""
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    results: List[float] = []

    for task in asyncio.as_completed(tasks):
        results.append(await task)

    return results
