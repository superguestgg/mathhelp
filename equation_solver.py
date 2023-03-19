import matplotlib.pyplot as plt
import math
import numpy as np
import time


def f(x):
    return 1/math.tan(x+0.4) - x*x


def draw_function(function):
    plt.figure(figsize=(10, 10))
    x_points = np.linspace(-10, 10, 1000)
    y_points = list(map(function, x_points))
    plt.plot(x_points, y_points)
    plt.ylabel("Y")
    plt.xlabel("X")
    #plt.scatter([3/8], [F(3/8)], lw=5)
    plt.show()


def get_derivative_prak(function, x_point):
    differential_x = 0.00001
    return (function(x_point + differential_x) - function(x_point)) / differential_x


def bin_search(function, start_points, shift, equal_to=0):
    new_function = lambda x: function(x) - equal_to
    left, right = start_points
    left_y, right_y = map(new_function, start_points)
    counter = 0
    while True:
        counter += 1
        m = (left + right) / 2
        m_y = new_function(m)
        if m_y * right_y > 0:
            right = m
            right_y = m_y
        else:
            left = m
            left_y = m_y
        if abs(left_y) < shift:
            break
    return left, counter


def newton_search(function, start_points, shift):
    current_x = start_points[1]
    current_y = function(current_x)
    counter = 0
    while True:
        counter += 1
        deriv = get_derivative_prak(function, current_x)
        current_x -= current_y / deriv
        current_y = function(current_x)

        if abs(current_y) < shift:
            break
    return current_x, counter


def fixed_chord_search(function, start_points, shift):
    x0, x1 = start_points
    y0, y1 = map(function, start_points)
    counter = 0
    while True:
        counter += 1
        # (x-x0)*((y1-y0)/(x1-x0)) + y0 = 0 =>
        # x * (y1-y0) = x0 * (y1-y0) + y0 * (x1-x0) =>
        # x = (x0 * (y1-y0) + y0 * (x1-x0)) / (y1-y0)
        x1 = (x0 * (y1-y0) - y0 * (x1-x0)) / (y1-y0)
        y1 = function(x1)
        if abs(y1) < shift:
            break
    return x1, counter


def unfixed_chord_search(function, start_points, shift):
    x0, x1 = start_points
    y0, y1 = map(function, start_points)
    counter = 0
    while True:
        counter += 1
        # (x-x0)*((y1-y0)/(x1-x0)) + y0 = 0 =>
        # x * (y1-y0) = x0 * (y1-y0) + y0 * (x1-x0) =>
        # x = (x0 * (y1-y0) + y0 * (x1-x0)) / (y1-y0)
        new_x = (x0 * (y1-y0) - y0 * (x1-x0)) / (y1-y0)
        x0, y0 = x1, y1
        x1, y1 = new_x, function(new_x)
        if abs(y1) < shift:
            break
    return x1, counter


print(time.process_time())
# функция ctg периодическая, период = pi,
# в моей функции при x=-0.4+pi*k (k-целое число) значение неопределено,
# поэтому буду искать наименьшее положительное решение на промежутке -0.4, 2,714..,
# таким образом я найду наименьший положительный  корень,
# потому что f имеет ровно 1 решение на нем
# и оно гарантированно наименьшее положительное
# (очев, левая граница меньше ноляб првая - больше)

# функция, которая дана мне монотонна на (-0.4, 2,714),
# поэтому все методы работают на отрезке [-0.3, 2.7] корректно, независимо от начальных точек,
# поэтому буду брать крайние точки, как значения x для нахождения первых касательных и хорд
shift = 0.00005

print(f"bin_search function results:{bin_search(f, [-0.3, 2.7], shift)}"
       f"\n\t\t\t(result_x, iterations_count)\n")
# (2 вроде) у меня нет, но самый легкий метод
# 16 iterations

print(f"newton_search function results:\n{newton_search(f, [-0.3, 2.7], shift)}\n") # 1
# 7 iterations

print(f"fixed_chord_search function results:\n{fixed_chord_search(f, [-0.3, 2.7], shift)}\n") # 4
# 33 iterations

print(f"unfixed_chord_search function results:\n{unfixed_chord_search(f, [-0.3, 2.7], shift)}\n") # 5
# 5 iterations

print(time.process_time())

draw_function(f)