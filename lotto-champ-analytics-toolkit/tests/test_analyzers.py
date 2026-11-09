import unittest

from src.frequency_analyzer import analyze_frequency
from src.hot_cold_analyzer import analyze_hot_cold
from src.combination_generator import generate_combinations
from src.lottery_statistics import calculate_statistics
from examples.powerball_analysis import analyze_powerball


class TestLotteryAnalytics(unittest.TestCase):
    def test_frequency(self):
        self.assertEqual(
            analyze_frequency([[1, 2], [2, 3]]),
            [(2, 2), (1, 1), (3, 1)],
        )

    def test_hot_cold(self):
        hot, cold = analyze_hot_cold([[1, 1, 2], [2, 3]], top_n=1)
        self.assertEqual(hot, [(1, 2)])
        self.assertEqual(cold, [(3, 1)])

    def test_combinations(self):
        self.assertEqual(
            generate_combinations([3, 1, 2, 2], size=2),
            [(1, 2), (1, 3), (2, 3)],
        )

    def test_statistics_empty(self):
        self.assertIsNone(calculate_statistics([]))

    def test_powerball(self):
        result = analyze_powerball([
            {"white": [1, 2, 3, 4, 5], "powerball": 9},
            {"white": [1, 2, 6, 7, 8], "powerball": 9},
        ])
        self.assertEqual(result["most_common_powerball"], [(9, 2)])


if __name__ == "__main__":
    unittest.main()
