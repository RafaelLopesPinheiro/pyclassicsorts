# pyclassicsorts

A small, well-organized Python package containing classic sorting algorithms:
- Merge sort
- Quick sort
- Selection sort
- Bubble sort

Goals:
- Clear, testable implementations
- Modular package layout
- Simple benchmark script and unit tests

Quick start:
1. Install dev dependencies:
   python -m pip install -e .[dev]

2. Run tests:
   pytest

3. Try the algorithms:
   >>> from sorts import merge_sort, quick_sort
   >>> merge_sort([3,1,2])
   [1,2,3]

Project layout:
- sorts/algorithms: algorithm implementations
- sorts/benchmarks.py: simple timing comparisons
- tests/: unit tests using pytest

License: MIT