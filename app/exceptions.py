class OperationError(Exception):
    """Raised when an invalid or unsupported operation is requested."""
    pass

class ValidationError(Exception):
    """Raised when input validation fails (e.g., invalid number or range)."""
    pass
