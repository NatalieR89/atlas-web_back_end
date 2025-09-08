#!/usr/bin/env python3
"""Type-annotated function that returns a tuple with a str and the square"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Return a tuple where first element is k and second is v squared as a float"""
    return (k, float(v ** 2))
