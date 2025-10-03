import random
import pytest

from sorts.algorithms import merge_sort, quick_sort, selection_sort, bubble_sort

ALGOS = [merge_sort, quick_sort, selection_sort, bubble_sort]


@pytest.mark.parametrize("algo", ALGOS)
def test_empty_and_single(algo):
    assert algo([]) == []
    assert algo([1]) == [1]


@pytest.mark.parametrize("algo", ALGOS)
def test_sorted_property(algo):
    for _ in range(30):
        arr = [random.randint(-50, 50) for _ in range(random.randint(0, 50))]
        expected = sorted(arr)
        out = algo(arr)
        assert out == expected


@pytest.mark.parametrize("algo", ALGOS)
def test_with_duplicates(algo):
    arr = [5, 1, 3, 5, 2, 5, 1]
    assert algo(arr) == sorted(arr)