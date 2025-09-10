#!/usr/bin/env python3
"""Create asyncio.Task objects from wait_random coroutine."""

import asyncio
from importlib import import_module

# Dynamically import wait_random
module = import_module("0-basic_async_syntax")
wait_random = module.wait_random

def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Returns an asyncio.Task object that wraps the wait_random coroutine
    with the given max_delay.
    """
    return asyncio.create_task(wait_random(max_delay))
