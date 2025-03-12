import sys

from solver import quadratic_equation_solver

def file_mode(filename):
    try:
        with open(filename, 'r') as f:
            line = f.readline().strip()
            parts = line.split()
            if len(parts) != 3:
                print('Invalid file format', file=sys.stderr)
                sys.exit(1)

            a, b, c = map(float, parts)

            print(f"Equation is: ({a}) x^2 + ({b}) x + ({c}) = 0")
            quadratic_equation_solver(a, b, c)

    except ValueError as e:
        print(f"Error: {e}")

    except FileNotFoundError:
        print("File not found")
