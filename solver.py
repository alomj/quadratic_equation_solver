import math


def quadratic_equation_solver(a, b, c):

    if a == 0:
        print("Invalid input: a cannot be zero in a quadratic equation.")
        return

    d = (b ** 2) - (4 * a * c)

    if d > 0:
        print('There are 2 roots:')
        x1 = (-b + math.sqrt(d)) / (2 * a)
        x2 = (-b - math.sqrt(d)) / (2 * a)
        print(f'X1 = {x1}, X2 = {x2}')
    elif d == 0:
        print('There is only one root')
        x1 = (-b + math.sqrt(d)) / (2 * a)
        print(f'X1 = {x1}')

    else:
        print("There are no roots")
