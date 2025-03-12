import math


def quadratic_equation_solver(a, b, c):
    d = (b ** 2) - (4 * a * c)
    if d > 0:
        print("There are 2 roots.")
        x1 = (-b + math.sqrt(d)) / (2 * a)
        x2 = (-b - math.sqrt(d)) / (2 * a)
        print(f'x1 = {x1}\nx\n x2 = {x2}\n')

    elif d == 0:
        print("There is 1 root.")
        x1 = (-b + math.sqrt(d)) / (2 * a)
        print(f"x1 = {x1}\n")

    else:
        print("There is no roots")

