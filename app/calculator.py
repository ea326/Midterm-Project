from app.operations import Addition, Subtraction, Multiplication, Division, Power, Root, Modulus, IntegerDivision, Percentage

class OperationFactory:
    @staticmethod
    def create(operation_type):
        if operation_type == "add":
            return Addition()
        elif operation_type == "subtract":
            return Subtraction()
        elif operation_type == "multiply":
            return Multiplication()
        elif operation_type == "divide":
            return Division()
        elif operation_type == "power":
            return Power()
        elif operation_type == "root":
            return Root()
        elif operation_type == "modulus":
            return Modulus()
        elif operation_type == "int_divide":
            return IntegerDivision()
        elif operation_type == "percent":
            return Percentage()
        else:
            raise ValueError(f"Invalid operation type: {operation_type}")
