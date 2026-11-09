from statistics import mean
from typing import Iterable, Optional, Dict


def calculate_statistics(draws: Iterable[Iterable[int]]) -> Optional[Dict[str, float]]:
    """Calculate descriptive statistics for all numbers in the supplied draws."""
    numbers = [number for draw in draws for number in draw]

    if not numbers:
        return None

    return {
        "total_numbers": len(numbers),
        "average": round(mean(numbers), 2),
        "minimum": min(numbers),
        "maximum": max(numbers),
        "unique_numbers": len(set(numbers)),
    }


if __name__ == "__main__":
    sample_draws = [
        [5, 12, 18, 27, 34, 45],
        [3, 14, 19, 30, 41, 49],
        [7, 15, 22, 28, 35, 42],
    ]
    print(calculate_statistics(sample_draws))
