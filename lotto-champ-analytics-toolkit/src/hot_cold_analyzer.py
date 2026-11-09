from collections import Counter
from typing import Iterable, List, Tuple


def analyze_hot_cold(
    draws: Iterable[Iterable[int]], top_n: int = 5
) -> Tuple[List[Tuple[int, int]], List[Tuple[int, int]]]:
    """Return the most- and least-frequent observed numbers.

    'Hot' and 'cold' describe only the supplied historical sample. They do
    not indicate that a number is more or less likely in a future draw.
    """
    if top_n < 1:
        raise ValueError("top_n must be at least 1")

    frequency = Counter(number for draw in draws for number in draw)
    if not frequency:
        return [], []

    hot = frequency.most_common(top_n)
    cold = sorted(frequency.items(), key=lambda item: (item[1], item[0]))[:top_n]
    return hot, cold


if __name__ == "__main__":
    sample_draws = [
        [4, 12, 18, 25, 33, 42],
        [4, 12, 19, 25, 34, 42],
        [7, 15, 18, 25, 33, 49],
        [4, 12, 18, 30, 33, 42],
    ]

    hot, cold = analyze_hot_cold(sample_draws)
    print("Hot numbers:", hot)
    print("Cold numbers:", cold)
