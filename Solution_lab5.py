from scipy import optimize
import numpy as np
from tabulate import tabulate

lst = np.loadtxt("sol_lab5_input.txt", dtype='i', delimiter=',')

minimum = np.min(lst, axis=1)
maximum = np.max(lst, axis=0)
point = 0

A_maxmin = np.max(minimum)

B_minmax = np.min(maximum)

if A_maxmin != B_minmax:
    no_point = "Сідлова точка відсутня!"

lst_del = np.delete(lst, 2, 0)
lst_del1 = np.delete(lst_del, 3, 0)
lst_del2 = np.delete(lst_del1, 0, 1)
lst_del3 = np.delete(lst_del2, 1, 1)
lst_del4 = np.delete(lst_del3, 1, 1)

# Симплекс метод
func = [1, 1]

left_part = [[-lst_del4[0, 0], -lst_del4[0, 1]],
             [-lst_del4[1, 0], -lst_del4[1, 1]],
             [-lst_del4[2, 0], -lst_del4[2, 1]]]

right_part = [-1, -1, -1]

bound = [(0, float("inf")),
         (0, float("inf"))]

min = optimize.linprog(c=func, A_ub=left_part, b_ub=right_part,
                       bounds=bound,
                       method="simplex")
res = round(1 / min.fun, 2)

print("Вхідна матриця:")
print(tabulate(headers=['', '', ''], tabular_data=[
    [lst[0][0], lst[0][1], lst[0][2], lst[0][3], lst[0][4]],
    [lst[1][0], lst[1][1], lst[1][2], lst[1][3], lst[1][4]],
    [lst[2][0], lst[2][1], lst[2][2], lst[2][3], lst[2][4]],
    [lst[3][0], lst[3][1], lst[3][2], lst[3][3], lst[3][4]],
    [lst[4][0], lst[4][1], lst[4][2], lst[4][3], lst[4][4]]
]))

print("Cпрощена матриця гри: ")
print(lst_del4)
print(f'Ціна гри розрахована симплекс-методом: {res}')

if A_maxmin != B_minmax:
    print(f'Нижня ціна гри: {A_maxmin}')
    print(f'Верхня ціна гри: {B_minmax}')
    print(no_point)
else:
    print(f'Нижня ціна гри: {A_maxmin}')
    print(f'Верхня ціна гри: {B_minmax}')
    print(f'Сідлова точка: {point}')

print(f'Межі ціни гри: [{A_maxmin};{B_minmax}]')

