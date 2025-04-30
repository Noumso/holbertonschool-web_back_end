#!/usr/bin/env python3
"""
This module contains an asynchronous generator function that
yields 10 random numbers between 0 and 10 with a 1-second delay between each.
"""

import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """
    Coroutine that yields a random float between 0 and 10,
    10 times, with a 1-second asynchronous delay between each.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
