"""
Convenience CLI to run the sorting benchmarks.

Place this file at the project root (next to pyproject.toml, README.md).
Run examples:
  python main.py --list
  python main.py --size 1000 --repeats 5
  python main.py --algo merge_sort --size 2000 --repeats 3 --seed 42

Note: this expects the benchmark module to be available as sorts.benchmarks.
If your file is currently named sorts/benchmark.py, rename it to sorts/benchmarks.py.
"""
import argparse
import random
import sys
from typing import Dict, Callable, List

try:
    from sorts.benchmarks import ALGORITHMS, time_algo  # type: ignore
except Exception as exc:
    print("ERROR: could not import sorts.benchmarks. Make sure you run this from the project root")
    print("and that sorts/benchmarks.py exists (not sorts/benchmark.py).")
    print("Detailed error:", exc)
    sys.exit(2)


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Run classic sorting algorithm benchmarks.")
    p.add_argument(
        "--size",
        "-n",
        type=int,
        default=500,
        help="Number of elements in the random input (default: 500)",
    )
    p.add_argument(
        "--repeats",
        "-r",
        type=int,
        default=3,
        help="Number of repetitions to average timing (default: 3)",
    )
    p.add_argument(
        "--algo",
        "-a",
        type=str,
        default="all",
        help='Algorithm to run (name from --list) or "all" to run every algorithm (default: all)',
    )
    p.add_argument(
        "--seed",
        "-s",
        type=int,
        default=None,
        help="Optional random seed for reproducible inputs",
    )
    p.add_argument(
        "--list",
        action="store_true",
        dest="list_algos",
        help="List available algorithm names and exit",
    )
    return p.parse_args()


def run_single(name: str, fn: Callable[[List[int]], List[int]], data: List[int], repeats: int) -> float:
    avg = time_algo(fn, data, repeats=repeats)
    print(f"{name:15s}: {avg:.6f}s")
    return avg


def main() -> None:
    args = parse_args()
    if args.list_algos:
        print("Available algorithms:")
        for name in ALGORITHMS.keys():
            print(" -", name)
        return

    if args.seed is not None:
        random.seed(args.seed)

    size = args.size
    repeats = args.repeats
    data = [random.randint(0, size) for _ in range(size)]

    if args.algo.lower() == "all":
        print(f"Benchmarking all algorithms (size={size}, repeats={repeats})")
        for name, fn in ALGORITHMS.items():
            run_single(name, fn, data, repeats)
    else:
        name = args.algo
        if name not in ALGORITHMS:
            print(f"Unknown algorithm: {name!r}")
            print("Use --list to see available algorithm names.")
            sys.exit(2)
        print(f"Benchmarking {name} (size={size}, repeats={repeats})")
        run_single(name, ALGORITHMS[name], data, repeats)


if __name__ == "__main__":
    main()