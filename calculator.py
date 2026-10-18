"""A simple and robust Python calculator with input validation and zero-division handling.

Designed for beginners, demonstrating modular functions, exception handling,
and clean command-line interaction.
"""


def add(a: float, b: float) -> float:
    """Return the sum of two numbers."""
    return a + b


def subtract(a: float, b: float) -> float:
    """Return the difference of two numbers (a - b)."""
    return a - b


def multiply(a: float, b: float) -> float:
    """Return the product of two numbers."""
    return a * b


def divide(a: float, b: float) -> float:
    """Return the quotient of two numbers (a / b).

    Raises:
        ZeroDivisionError: If the divisor (b) is 0.
    """
    if b == 0:
        raise ZeroDivisionError("Error: Division by zero is undefined.")
    return a / b


def calculate(operation: str, a: float, b: float) -> float:
    """Perform the specified calculation on two numbers.

    Supported operations:
      - Addition: '+', '1', 'add'
      - Subtraction: '-', '2', 'subtract'
      - Multiplication: '*', '3', 'multiply'
      - Division: '/', '4', 'divide'

    Raises:
        ValueError: If the operation symbol/name is unsupported.
        ZeroDivisionError: If attempting to divide by zero.
    """
    op = operation.strip().lower()

    if op in ("+", "1", "add"):
        return add(a, b)
    elif op in ("-", "2", "subtract"):
        return subtract(a, b)
    elif op in ("*", "3", "multiply"):
        return multiply(a, b)
    elif op in ("/", "4", "divide"):
        return divide(a, b)
    else:
        raise ValueError(f"Unknown operation: '{operation}'")


def get_number(prompt: str) -> float:
    """Prompt user until a valid floating-point number or integer is entered."""
    while True:
        raw_input = input(prompt).strip()
        try:
            return float(raw_input)
        except ValueError:
            print("  [!] Invalid input. Please enter a valid number (e.g., 10, -3.5, 0).")


def get_operation() -> str:
    """Prompt user to choose a valid arithmetic operation or quit."""
    valid_ops = {"+", "-", "*", "/", "1", "2", "3", "4", "5", "q", "exit", "quit"}
    while True:
        print("\nSelect an operation:")
        print("  1. Addition       (+)")
        print("  2. Subtraction    (-)")
        print("  3. Multiplication (*)")
        print("  4. Division       (/)")
        print("  5. Quit           (q)")
        choice = input("Enter choice (1-5 or +, -, *, /, q): ").strip().lower()

        if choice in valid_ops:
            return choice
        print("  [!] Invalid selection. Please enter 1, 2, 3, 4, 5, or +, -, *, /, q.")


def main():
    """Run the interactive calculator loop."""
    print("=" * 45)
    print("        WELCOME TO PYTHON CALCULATOR        ")
    print("=" * 45)

    while True:
        try:
            op_choice = get_operation()

            # Check if user wants to exit
            if op_choice in ("5", "q", "exit", "quit"):
                print("\nThank you for using the calculator. Goodbye!")
                break

            # Get operands with validation
            num1 = get_number("\nEnter the first number: ")
            num2 = get_number("Enter the second number: ")

            # Calculate and display result
            result = calculate(op_choice, num1, num2)

            # Format float nicely (e.g. 5.0 -> 5 if it's a whole number)
            formatted_result = int(result) if result.is_integer() else result
            print(f"\n>>> Result: {formatted_result}")

        except ZeroDivisionError as err:
            print(f"\n  [!] Math Error: {err}")
        except ValueError as err:
            print(f"\n  [!] Input Error: {err}")
        except (KeyboardInterrupt, EOFError):
            print("\n\nOperation cancelled. Goodbye!")
            break


if __name__ == "__main__":
    main()
