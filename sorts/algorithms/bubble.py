from typing import List, Sequence, TypeVar

T = TypeVar("T")


def bubble_sort(arr: Sequence[T]) -> List[T]:
    """
    Classic bubble sort (optimized with early exit).
    O(n^2) time. Educational purposes only.
    """
    out = list(arr)
    n = len(out)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if out[j] > out[j + 1]:
                out[j], out[j + 1] = out[j + 1], out[j]
                swapped = True
        if not swapped:
            break
    return out