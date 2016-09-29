from scipy.optimize import linprog
import numpy as np


A = np.array([[1, -5, 3, 1, 0, 0],
              [4, -1, 1, 0, 1, 0],
              [2, 4, 2, 0, 0, 6]])
b = np.array([-8, 22, 30])
c = np.array([7, -2, 6, 0, 5, 2])
d_low = [2, 1, 0, 0, 1, 1]
d_high = [6, 6, 5, 2, 4, 6]

#
# A = np.array([[1,  0,  2,  2,  -3,  3],
#               [0,  1,  0,  -1,  0,  1],
#               [1,  0,  1,  3,  2,  1]])
# b = np.array([15, 0, 13])
# c = np.array([3,  0.5,  4,  4,  1,  5])
# d_low = [0, 0, 0, 0, 0, 0]
# d_high = [3, 5, 4, 3, 3, 4]

res = linprog(-c, A, b, bounds=zip(d_low, d_high))
print(np.dot(c, res.x))
print res.fun
print res.x




# def is_integer(value):
#     if abs(round(value) - value) < 1e-6:
#         return True
#     else:
#         return False
#
#
# def is_integers(values):
#     if all(is_integer(value) for value in values):
#         return True
#     else:
#         return False
#
#
# def get_first_fractional(values):
#     for i in range(0, len(values)):
#         if is_integer(values[i]) is False:
#             return i

