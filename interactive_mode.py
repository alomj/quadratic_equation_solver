import sys
from solver import quadratic_equation_solver

def get_valid_float(prompt):
        user_input = input(prompt)
        try:
            return float(user_input)
        except ValueError:
            print(f"Error. Expected a valid real number, got {user_input} instead", file=sys.stdout)

def interactive_mode():
        a = get_valid_float("a = ")
        b = get_valid_float("b = ")
        c = get_valid_float("c = ")

        print(f"Equation is: ({a}) x^2 + ({b}) x + ({c}) = 0")
        quadratic_equation_solver(a, b, c)

if __name__ == '__main__':
    interactive_mode()
