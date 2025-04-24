#!/usr/bin/env python3
"""measure_time function with n and max_delay arguments"""
import time
import asyncio

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """measures the total execution time for wait_n(n, max_delay),
     and returns total_time / n. Return a float"""
    start_time = time.time()

    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()
    elapse_time = end_time - start_time
    return elapse_time / n
