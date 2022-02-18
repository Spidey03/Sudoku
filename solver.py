import numpy as np
import constants

class Solver:
    def __init__(self, problem):
        self.problem = problem

    def validate_problem(self):
        if not self.problem.shape == (9, 9):
            raise Exception("Sudoku Problem is not in correct format: expected 9 * 9")

    def get_solution(self):
        # self.validate_problem()
        pos = self.get_unsolved_box()
        if not pos:
            print("Find solution!")
            return True

    
    def get_unsolved_box(self) -> tuple:
        """Returns first unsolved box top to bottom, left to right

        Returns:
            tuple: position of unsolved box
        """
        row_indices, col_indices = np.where(self.problem == 10)
        if row_indices and col_indices:
            return row_indices[0], col_indices[0]

    def _is_valid_number(position: tuple, val: int):
        for i in range(constants.ROWS+1):
            pass
        
        for i in range(constants.COLS+1):
            pass