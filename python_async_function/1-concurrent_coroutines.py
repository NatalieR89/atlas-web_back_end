#!/usr/bin/env python3
"""Concurrent coroutines example: wait_n coroutine using wait_random."""

import asyncio
from basic_async_syntax import wait_random  # Correct import

from typing import List

async def wait_n(n: int, max_delay: int) -> List[float]:
    """Spawn wait_random n times with max_delay and return delays in order of completion."""
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    results: List[float] = []

    for task in asyncio.as_completed(tasks):
        delay = await task
        results.append(delay)

    return results
