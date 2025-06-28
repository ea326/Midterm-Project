from app.operations import Addition, Subtraction, Multiplication, Division

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
        else:
            raise ValueError(f"Invalid operation type: {operation_type}")
