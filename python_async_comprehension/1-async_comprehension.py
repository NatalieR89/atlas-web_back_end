#!/usr/bin/env python3
"""
Module 1-async_comprehension
Contains the coroutine async_comprehension that collects 10 random
numbers from async_generator using async comprehension.
"""

from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Coroutine that collects 10 random numbers from async_generator
    using an async comprehension, then returns them.
    """
    return [i async for i in async_generator()]
