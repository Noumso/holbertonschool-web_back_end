#!/usr/bin/env python3
"""Take the code from wait_n and alter it into
a new function task_wait_n. The code is nearly
identical to wait_n except task_wait_random
is being called"""
import asyncio
import random
from typing import List


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """returns a list of all the delays"""
    value_list: List[float] = []
    all_list: List[float] = []

    for i in range(n):
        value_list.append(task_wait_random(max_delay))
    for task in asyncio.as_completed(value_list):
        result = await task
        all_list.append(result)
    return all_list
