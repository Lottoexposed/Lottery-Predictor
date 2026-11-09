from collections import Counter
from typing import Iterable, List, Tuple


def analyze_frequency(draws: Iterable[Iterable[int]]) -> List[Tuple[int, int]]:
    """Return (number, appearance_count) pairs, most frequent first."""
    numbers = Counter(number for draw in draws for number in draw)
    return numbers.most_common()


if __name__ == "__main__":
    historical_draws = [
        [5, 12, 18, 27, 34, 45],
        [3, 12, 19, 27, 41, 45],
        [5, 14, 18, 30, 34, 42],
        [5, 12, 22, 27, 34, 49],
    ]

    print("Lottery Number Frequency Analysis")
    for number, frequency in analyze_frequency(historical_draws):
        print(f"Number {number}: {frequency} appearances")
