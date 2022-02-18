class Solver:
    def __init__(self, problem):
        self.problem = problem

    def validate_problem(self):
        if not self.problem.shape == (9, 9):
            raise Exception("Sudoku Problem is not in correct format: expected 9 * 9")

    def get_solution(self):
        self.validate_problem()
