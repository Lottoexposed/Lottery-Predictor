from collections import Counter
from typing import Dict, Iterable, List


def analyze_powerball(draws: Iterable[Dict[str, List[int]]]) -> dict:
    """Count white-ball and red Powerball appearances in supplied sample draws."""
    white_balls = Counter()
    red_balls = Counter()

    for draw in draws:
        white_balls.update(draw["white"])
        red_balls.update([draw["powerball"]])

    return {
        "most_common_white": white_balls.most_common(10),
        "most_common_powerball": red_balls.most_common(5),
    }


if __name__ == "__main__":
    sample_draws = [
        {"white": [5, 12, 23, 34, 61], "powerball": 18},
        {"white": [8, 12, 27, 34, 65], "powerball": 18},
        {"white": [5, 19, 23, 42, 61], "powerball": 7},
    ]

    print(analyze_powerball(sample_draws))
