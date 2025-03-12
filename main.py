import sys
from file_mode import file_mode
from interactive_mode import interactive_mode


def main():
    while True:
        print("Welcome to Quadratic Equation Solver")
        print("Select mode:")
        print("1 - Interactive mode")
        print("2 - File mode")
        print('3 - Exit')
        try:
            mode = int(input("Enter your choice (1, 2 or 3): "))

            if mode == 1:
                interactive_mode()

            elif mode == 2:
                filename = input("Enter filename: ").strip()
                if not filename:
                    print("Error: Filename cannot be empty.", file=sys.stderr)
                    sys.exit(1)

                file_mode(filename)

            elif mode == 3:
                print("Exiting the program. Goodbye!")
                break

            else:
                print("Invalid choice. Please enter 1, 2 or 3.", file=sys.stderr)

        except ValueError:
            print("Invalid input. Please enter a number (1, 2 or 3).", file=sys.stderr)
            sys.exit(1)


if __name__ == "__main__":
    main()
