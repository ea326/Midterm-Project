import pytest
from app.calculator import OperationFactory

def test_addition():
    op = OperationFactory.create("add")
    assert op.execute(4, 3) == 7
    assert op.execute(-1, 1) == 0
    assert op.execute(0, 0) == 0

def test_subtraction():
    op = OperationFactory.create("subtract")
    assert op.execute(10, 5) == 5
    assert op.execute(5, 10) == -5

def test_multiplication():
    op = OperationFactory.create("multiply")
    assert op.execute(2, 3) == 6
    assert op.execute(0, 100) == 0

def test_division():
    op = OperationFactory.create("divide")
    assert op.execute(10, 2) == 5
    assert op.execute(9, 3) == 3

def test_division_by_zero():
    op = OperationFactory.create("divide")
    with pytest.raises(ZeroDivisionError):
        op.execute(5, 0)

def test_power():
    op = OperationFactory.create("power")
    assert op.execute(2, 3) == 8
    assert op.execute(5, 0) == 1
    assert op.execute(4, 0.5) == 2  # square root

def test_invalid_operation():
    with pytest.raises(ValueError):
        OperationFactory.create("invalid_op")
