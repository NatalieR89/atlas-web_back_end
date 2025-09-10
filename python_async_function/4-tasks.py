#!/usr/bin/env python3
"""Concurrent tasks example: task_wait_n coroutine using task_wait_random."""

import asyncio
from importlib import import_module
from typing import List

# Dynamically import task_wait_random from 3-tasks
module = import_module("3-tasks")
task_wait_random = module.task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawn task_wait_random n times with max_delay and return delays in
    order of completion.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    results: List[float] = []

    for task in asyncio.as_completed(tasks):
        results.append(await task)

    return results
