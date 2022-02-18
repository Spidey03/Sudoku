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

        for num in range(1, constants.ROWS+1):
            if self._is_valid_number(pos=pos, val=num):
                self.problem[pos[0]][pos[1]] = num

                if self.get_solution():
                    return True
                self.problem[pos[0]][pos[1]] = 0
        return False

    def get_unsolved_box(self) -> tuple:
        """Returns first unsolved box top to bottom, left to right

        Returns:
            tuple: position of unsolved box
        """
        row_indices, col_indices = np.where(self.problem == 10)
        if row_indices and col_indices:
            return row_indices[0], col_indices[0]

    def _is_valid_number(self, pos: tuple, val: int):
        
        # Check if row already has the number
        for i in range(constants.COLS+1):
            if self.problem[pos[0]][i] == val and pos[1] != i:
                return False

        # Check if column already has the number
        for i in range(constants.ROWS+1):
            if self.problem[i][pos[1]] == val and pos[0] != i:
                return False

        # find box
        box_y = pos[0]//3
        box_x = pos[1]//3

        for row in range(box_y*3, box_y+3):
            for col in range(box_x*3, box_x*3+3):
                if self.problem[row][col] == val and (row, col) != pos:
                    return False
        return True