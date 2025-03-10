"""
This module contains the OperationExecutor class, which encapsulates the shared logic for executing an operation.
"""
from decimal import Decimal, InvalidOperation


def _get_decimal_input(prompt: str) -> Decimal:
    raw_input = input(prompt)
    return Decimal(raw_input)


class OperationExecutor:
    """
    Encapsulates the shared logic for executing an operation:
      - Reading two decimal inputs from the user.
      - Executing the provided operation.
      - Handling errors and displaying results.
    """
    def __init__(self, operation_callable, operation_name: str):
        self.operation_callable = operation_callable
        self.operation_name = operation_name

    def execute(self):
        """
        Executes the operation by reading two decimal inputs from the user and displaying the result.
        """
        try:
            a = _get_decimal_input("Enter the first number: ")
            b = _get_decimal_input("Enter the second number: ")
        except (InvalidOperation, ValueError):
            print("Invalid input. Please enter valid decimal numbers.")
            return

        try:
            result = self.operation_callable(a, b)
            print(f"Result of {self.operation_name}: {result}")
        except ZeroDivisionError:
            print("Error: Division by zero.")
        except Exception as e:
            print(f"An error occurred: {e}")

