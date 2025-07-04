from datetime import datetime
from app.calculator_config import CALCULATOR_PRECISION

class Calculation:
    def __init__(self, operation, a, b, result):
        self.operation = operation
        self.a = a
        self.b = b
        self.result = round(result, CALCULATOR_PRECISION)
        self.timestamp = datetime.now()

    def __str__(self):
        return f"{self.timestamp.strftime('%Y-%m-%d %H:%M:%S')} | {self.operation.__class__.__name__}({self.a}, {self.b}) = {self.result}"
