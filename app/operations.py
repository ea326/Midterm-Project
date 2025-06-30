class Addition:
    def execute(self, a, b):
        return a + b

class Subtraction:
    def execute(self, a, b):
        return a - b

class Multiplication:
    def execute(self, a, b):
        return a * b

class Division:
    def execute(self, a, b):
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return a / b

class Power:
    def execute(self, a, b):
        return a ** b

class Root:
    def execute(self, a, b):
        if b == 0:
            raise ValueError("Cannot take the 0th root.")
        return a ** (1 / b)

class Modulus:
    def execute(self, a, b):
        if b == 0:
            raise ValueError("Cannot perform modulus by zero.")
        return a % b

class IntegerDivision:
    def execute(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a // b
    
class Percentage:
    def execute(self, a, b):
        if b == 0:
            raise ValueError("Cannot calculate percentage with denominator zero.")
        return (a / b) * 100
    
class AbsoluteDifference:
    def execute(self, a, b):
        return abs(a - b)

