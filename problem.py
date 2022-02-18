import numpy as np
import constants
from solver import Solver


def from_file():
    with open(constants.FILE_NAME, 'r') as f:
        rows = f.readlines()
        problem = np.array([row.strip().split() for row in rows], int)
    return problem

def from_input():
    problem = np.array([input().strip().split() for _ in range(ROWS)], int)
    return problem


sudoku_problem = from_file()
if not sudoku_problem.any():
    sudoku_problem = from_input()

print(sudoku_problem)
Solver(problem=sudoku_problem).get_solution()