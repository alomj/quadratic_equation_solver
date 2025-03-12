import math


def quadratic_equation_solver(a, b, c):
    x1, x2 = 0, 0
    d = (b ** 2) - (4 * a * c)
    if d > 0:
        x1 = (-b + math.sqrt(d)) / (2 * a)
        x2 = (-b - math.sqrt(d)) / (2 * a)
    elif d == 0:
        x1 = (-b + math.sqrt(d)) / (2 * a)
        return x1
    else:
        print("There is no roots")
    return x1, x2


