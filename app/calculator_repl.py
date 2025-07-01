import logging
from app.input_validators import validate_input
from app.calculation import Calculation
from app.calculator import OperationFactory
from app.history import history
from app.logger import LoggingObserver
from app.auto_save import AutoSaveObserver
from app.exceptions import ValidationError

history.register_observer(LoggingObserver())
history.register_observer(AutoSaveObserver())

def calculator_repl():
    print("Welcome to the calculator.")
    print("Usage: operation number1 number2 (e.g., add 4 5)")
    print("Available operations: add, subtract, multiply, divide, power, root, modulus, int_divide, percent, abs_diff")
    print("Other commands: history, undo, redo, clear, save, load, help, exit")

    while True:
        try:
            user_input = input("Enter command (or 'exit' to quit): ").strip().lower()
            if user_input == "exit":
                print("Goodbye.")
                break

            if user_input == "history":
                for item in history.get_history():
                    print(item)
                continue

            if user_input == "undo":
                undone = history.undo()
                print(f"Undid: {undone}")
                continue

            if user_input == "redo":
                redone = history.redo()
                print(f"Redid: {redone}")
                continue

            if user_input == "clear":
                history.clear()
                print("History cleared.")
                continue

            if user_input == "save":
                history.save_to_file()
                print("History saved.")
                continue

            if user_input == "load":
                history.load_from_file()
                print("History loaded.")
                continue

            if user_input == "help":
                print("Supported commands:")
                print("  add, subtract, multiply, divide, power, root, modulus, int_divide, percent, abs_diff")
                print("  history - Show calculation history")
                print("  clear   - Clear history")
                print("  undo    - Undo last calculation")
                print("  redo    - Redo last undone calculation")
                print("  save    - Save history to file")
                print("  load    - Load history from file")
                print("  help    - Show this help menu")
                print("  exit    - Exit the calculator")
                continue

            parts = user_input.split()
            if len(parts) != 3:
                print("Invalid input. Use: operation number1 number2")
                continue

            op_type, num1, num2 = parts
            a = validate_input(num1)
            b = validate_input(num2)

            operation = OperationFactory.create(op_type)
            result = operation.execute(a, b)
            print(f"Result: {result}\n")

            calculation = Calculation(operation, a, b, result)
            history.add_calculation(calculation)

        except ValidationError as ve:
            logging.error(f"ValidationError: {ve}")
            print(f"Validation error: {ve}")

        except ValueError as ve:
            logging.error(f"ValueError: {ve}")
            print(f"Error: {ve}")

        except ZeroDivisionError:
            logging.error("ZeroDivisionError: Cannot divide by zero.")
            print("Error: Cannot divide by zero.")

        except Exception as e:
            logging.exception(f"Unexpected error: {e}")
            print(f"Unexpected error: {e}")
