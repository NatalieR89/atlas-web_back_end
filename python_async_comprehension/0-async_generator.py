#!/usr/bin/env python3
"""
Module 0-async_generator
Contains a coroutine that loops 10 times, each time waits 1 second,
then yields a random number between 0 and 10.
"""

import asyncio
import random
from typing import AsyncGenerator

async def async_generator() -> AsyncGenerator[float, None]:
    """Coroutine that yields 10 random numbers asynchronously."""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
