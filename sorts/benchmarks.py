"""
Simple benchmark script to compare the implementations on random inputs.
Run: python -m sorts.benchmarks
"""
import random
import time
from typing import Callable, List

from sorts.algorithms import merge_sort, quick_sort, selection_sort, bubble_sort

ALGORITHMS = {
    "merge_sort": merge_sort,
    "quick_sort": quick_sort,
    "selection_sort": selection_sort,
    "bubble_sort": bubble_sort,
}


def time_algo(fn: Callable[[List[int]], List[int]], data: List[int], repeats: int = 3) -> float:
    times = []
    for _ in range(repeats):
        data_copy = list(data)
        t0 = time.perf_counter()
        fn(data_copy)
        t1 = time.perf_counter()
        times.append(t1 - t0)
    return sum(times) / len(times)


def run(size: int = 1000, repeats: int = 3):
    data = [random.randint(0, size) for _ in range(size)]
    print(f"Benchmark with size={size}")
    for name, fn in ALGORITHMS.items():
        avg = time_algo(fn, data, repeats=repeats)
        print(f"{name:15s}: {avg:.6f}s")


if __name__ == "__main__":
    run(size=500, repeats=5)