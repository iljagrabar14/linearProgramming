from scipy.optimize import linprog
import numpy as np


class IntegerSimplex(object):
    def __init__(self, A, b, c, d_min, d_max):
        self.A = A
        self.b = b
        self.c = c
        self.d_min = d_min
        self.d_max = d_max

        self.answer = [None, None, None, None, None, None]
        self.eps = 1e-8
        self.solution_exist = False
        self.best_cost = -np.inf

    def is_integer(self, value):
        if abs(round(value) - value) < self.eps:
            return True
        else:
            return False

    def is_integers(self, values):
        if all(self.is_integer(value) for value in values):
            return True
        else:
            return False

    def get_first_fractional(self, values):
        for i in range(0, len(values)):
            if self.is_integer(values[i]) is False:
                return i

    def branch_and_bounds(self, d_min, d_max):
        solution = linprog(-self.c, self.A, self.b, bounds=list(zip(d_min, d_max)))
        if solution.success:
            x = solution.x
            new_cost = np.dot(self.c, x)
        else:
            return

        if new_cost < self.best_cost:
            return

        if self.is_integers(x):
            self.solution_exist = True
            self.best_cost = new_cost
            for i in range(0, len(self.answer)):
                self.answer[i] = x[i]
            return
        else:
            i = self.get_first_fractional(x)
            l = np.floor(x[i])
            new_left_board = np.copy(d_min)
            new_right_board = np.copy(d_max)
            new_left_board[i] = l + 1
            new_right_board[i] = l
            self.branch_and_bounds(new_left_board, d_max)
            self.branch_and_bounds(d_min, new_right_board)

    def check_answer(self):
        self.branch_and_bounds(self.d_min, self.d_max)
        if self.solution_exist:
            return self
        else:
            return "NO ANSWER"


A = np.array([[1, -5, 3, 1, 0, 0],
              [4, -1, 1, 0, 1, 0],
              [2, 4, 2, 0, 0, 6]])
b = np.array([-8, 22, 30])
c = np.array([7, -2, 6, 0, 5, 2])
d_low = [2, 1, 0, 0, 1, 1]
d_high = [6, 6, 5, 2, 4, 6]

x0 = IntegerSimplex(A, b, c, d_low, d_high).check_answer()
print x0.answer
print np.dot(c, x0.answer)


