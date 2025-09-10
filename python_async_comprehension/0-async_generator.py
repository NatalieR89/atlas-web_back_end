#!/usr/bin/env python3
import random
from typing import Generator

def async_generator() -> Generator[float, None, None]:
    """
    Generator that yields 10 random numbers between 0 and 10.
    """
    for _ in range(10):
        yield random.uniform(0, 10)
