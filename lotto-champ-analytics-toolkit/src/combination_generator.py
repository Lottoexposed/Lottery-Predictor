from itertools import combinations
from typing import Iterable, List, Tuple


def generate_combinations(
    numbers: Iterable[int], size: int = 6
) -> List[Tuple[int, ...]]:
    """Generate unique combinations from a supplied number pool."""
    unique_numbers = sorted(set(numbers))

    if size <= 0 or size > len(unique_numbers):
        raise ValueError("size must be between 1 and the number of unique values")

    return list(combinations(unique_numbers, size))


if __name__ == "__main__":
    number_pool = [5, 12, 18, 27, 34, 42, 49]
    for combination in generate_combinations(number_pool, size=6):
        print(combination)
