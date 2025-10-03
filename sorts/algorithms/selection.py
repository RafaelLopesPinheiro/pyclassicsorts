from typing import List, Sequence, TypeVar

T = TypeVar("T")


def selection_sort(arr: Sequence[T]) -> List[T]:
    """
    Selection sort returning a new list.
    O(n^2) time, O(1) extra memory (besides copy).
    Good for teaching/demonstration only.
    """
    out = list(arr)
    n = len(out)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if out[j] < out[min_idx]:
                min_idx = j
        if min_idx != i:
            out[i], out[min_idx] = out[min_idx], out[i]
    return out