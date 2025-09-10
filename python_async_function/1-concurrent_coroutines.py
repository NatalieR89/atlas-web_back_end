#!/usr/bin/env python3
"""Concurrent coroutines example: wait_n coroutine using wait_random."""

import asyncio
import wait_random  # Import the previous coroutine

async def wait_n(n: int, max_delay: int) -> list[float]:
    """Spawn wait_random n times with max_delay and return delays in order of completion."""
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    results = []

    for task in asyncio.as_completed(tasks):
        delay = await task
        results.append(delay)

    return results
