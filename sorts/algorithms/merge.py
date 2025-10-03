from typing import List, Sequence, TypeVar

T = TypeVar("T")


def merge_sort(arr: Sequence[T]) -> List[T]:
    """
    Merge sort that returns a new sorted list.
    Stable and O(n log n) time.
    """
    items = list(arr)
    n = len(items)
    if n <= 1:
        return items

    mid = n // 2
    left = merge_sort(items[:mid])
    right = merge_sort(items[mid:])

    merged: List[T] = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    if i < len(left):
        merged.extend(left[i:])
    if j < len(right):
        merged.extend(right[j:])
    return merged