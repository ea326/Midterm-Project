from app.calculator_config import CALCULATOR_MAX_INPUT_VALUE
from app.exceptions import ValidationError

def validate_input(value):
    try:
        num = float(value)
    except ValueError:
        raise ValidationError(f"Invalid number: {value}")

    if abs(num) > CALCULATOR_MAX_INPUT_VALUE:
        raise ValidationError(f"Input value {num} exceeds max allowed: {CALCULATOR_MAX_INPUT_VALUE}")
    return num
