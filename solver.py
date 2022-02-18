import numpy as np
import constants

class Solver:
    def __init__(self, problem):
        self.header()
        self.problem = problem
        self.display_problem()

    def validate_problem(self):
        if not self.problem.shape == (9, 9):
            raise Exception("Sudoku Problem is not in correct format: expected 9 * 9")

    def get_final_solution(self):
        self.display_problem()
        if self.get_solution():
            self.display_problem(flush=True)
            print("Found Solution!!! 👆🏽")
        else:
            print("Sorry, Didn't find solution")

    def get_solution(self):
        self.validate_problem()
        pos = self.get_unsolved_box()
        if not pos:
            return True

        for num in range(1, constants.ROWS+1):
            if self._is_valid_number(pos=pos, val=num):
                self.problem[pos[0]][pos[1]] = num

                if self.get_solution():
                    return True
                self.problem[pos[0]][pos[1]] = 0
                self.display_problem(flush=True)
        return False

    def get_unsolved_box(self) -> tuple:
        """Returns first unsolved box top to bottom, left to right

        Returns:
            tuple: position of unsolved box
        """
        row_indices, col_indices = np.where(self.problem == 0)
        if row_indices.any() and col_indices.any():
            return row_indices[0], col_indices[0]

    def _is_valid_number(self, pos: tuple, val: int):
        
        # Check if row already has the number
        for i in range(constants.COLS):
            if self.problem[pos[0]][i] == val and pos[1] != i:
                return False

        # Check if column already has the number
        for i in range(constants.ROWS):
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

    def display_problem(self, flush=False, val: str = ""):
        repr = ""
        if flush == True:
            up = "\033[A" * 14
            repr = f"\r{up}"
        repr += '  - - - ' * 3 + '\n'
        for i in range(self.problem.shape[0]):
            if i!= 0 and i % 3 == 0:
                    repr += '  - - - ' * 3 + '\n'

            for j in range(self.problem.shape[1]):
                if j == 0 or j % 3 == 0:
                    repr += "| "
                repr += str(self.problem[i][j])
                if j == self.problem.shape[0]-1:
                    repr += ' |\n'
                else:
                    repr += ' '
        repr += '  - - - ' * 3 + '\n'
        print(repr)

    @staticmethod
    def header():
        print("""
░██████╗██╗░░░██╗██████╗░░█████╗░██╗░░██╗██╗░░░██╗
██╔════╝██║░░░██║██╔══██╗██╔══██╗██║░██╔╝██║░░░██║
╚█████╗░██║░░░██║██║░░██║██║░░██║█████═╝░██║░░░██║
░╚═══██╗██║░░░██║██║░░██║██║░░██║██╔═██╗░██║░░░██║
██████╔╝╚██████╔╝██████╔╝╚█████╔╝██║░╚██╗╚██████╔╝
╚═════╝░░╚═════╝░╚═════╝░░╚════╝░╚═╝░░╚═╝░╚═════╝░
""")