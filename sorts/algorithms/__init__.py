"""
Algorithms subpackage. Each algorithm is implemented in its own module.
"""
from .merge import merge_sort
from .quick import quick_sort
from .selection import selection_sort
from .bubble import bubble_sort

__all__ = ["merge_sort", "quick_sort", "selection_sort", "bubble_sort"]