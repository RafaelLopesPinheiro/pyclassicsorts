"""
Top-level package for pyclassicsorts.

Exports the main sorting functions for convenient import:
from sorts import merge_sort, quick_sort, selection_sort, bubble_sort
"""
from .algorithms import merge_sort, quick_sort, selection_sort, bubble_sort

__all__ = ["merge_sort", "quick_sort", "selection_sort", "bubble_sort"]