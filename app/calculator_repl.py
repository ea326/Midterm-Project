from app.calculator import OperationFactory

def calculator_repl():
    print("Welcome to the calculator.")
    print("Usage: operation number1 number2 (e.g., add 4 5)")
    print("Available operations: add, subtract, multiply, divide, power, root, modulus, int_divide, percent")

    while True:
        try:
            user_input = input("Enter command (or 'exit' to quit): ").strip().lower()
            if user_input == "exit":
                print("Goodbye.")
                break

            parts = user_input.split()
            if len(parts) != 3:
                print("Invalid input. Use: operation number1 number2")
                continue

            op_type, num1, num2 = parts
            a = float(num1)
            b = float(num2)

            operation = OperationFactory.create(op_type)
            result = operation.execute(a, b)
            print(f"Result: {result}\n")

        except ValueError as ve:
            print(f"Error: {ve}")
        except ZeroDivisionError:
            print("Error: Cannot divide by zero.")
        except Exception as e:
            print(f"Unexpected error: {e}")
