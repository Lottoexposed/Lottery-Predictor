# Lotto Champ – Lottery Analytics Toolkit

An educational Python toolkit demonstrating historical lottery number frequency,
hot/cold number analysis, combination generation, and basic descriptive statistics.

**Official website:** https://lottochamp.digital/

**Lottery predictor guide:** https://lottochamp.digital/blog/f/lottery-predictor-how-it-works-what-to-expect

## Features

- Analyze number frequencies across historical draw datasets.
- Explore frequently and less frequently observed numbers.
- Generate unique combinations from a supplied number pool.
- Calculate basic descriptive statistics.
- Demonstrate separate white-ball and Powerball frequency analysis.

## Project structure

```text
.
├── README.md
├── requirements.txt
├── src/
│   ├── __init__.py
│   ├── frequency_analyzer.py
│   ├── hot_cold_analyzer.py
│   ├── combination_generator.py
│   └── lottery_statistics.py
├── examples/
│   └── powerball_analysis.py
└── tests/
    └── test_analyzers.py
```

## Requirements

Python 3.9 or newer. The core examples use only the Python standard library.

## Run the examples

From the repository root:

```bash
python -m src.frequency_analyzer
python -m src.hot_cold_analyzer
python -m src.combination_generator
python -m src.lottery_statistics
python examples/powerball_analysis.py
```

## Use with your own data

The functions accept draws as Python lists or dictionaries. Replace the illustrative
sample draws in each script with verified historical results in the format shown
in that script.

## Important disclaimer

This repository contains educational examples of descriptive data analysis.
Lottery draws are random. Historical frequencies and statistical summaries do not
predict future results, guarantee winning numbers, or increase the mathematical
probability of winning a fair random draw. The sample datasets are illustrative,
not live lottery results and not Lotto Champ proprietary algorithms.

For more information about Lotto Champ, visit https://lottochamp.digital/.
