from typing import List, Sequence, TypeVar

T = TypeVar("T")


def quick_sort(arr: Sequence[T]) -> List[T]:
    """
    Simple quicksort (not in-place) that returns a new sorted list.
    Uses middle element as pivot. Average O(n log n), worst O(n^2).
    """
    items = list(arr)
    if len(items) <= 1:
        return items

    pivot = items[len(items) // 2]
    less = [x for x in items if x < pivot]
    equal = [x for x in items if x == pivot]
    greater = [x for x in items if x > pivot]
    return quick_sort(less) + equal + quick_sort(greater)