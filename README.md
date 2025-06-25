# Game of Fifteen solver

This repository contains a small Python script that brute forces solutions for the classic *Game of Fifteen*. The puzzle, also known as the 3x3 magic square, asks you to arrange the numbers 1–9 so that each row, column and diagonal sums to 15.

The script checks every possible combination of the digits and prints out the valid magic squares it finds. It is not optimised, but it demonstrates how a brute-force approach can uncover all eight solutions.

## Running

All you need is Python 3. Launch the search with:

```bash
python3 resolve_game_of_fifteen.py
```

The exhaustive search may take some time because every permutation of the digits is inspected.

