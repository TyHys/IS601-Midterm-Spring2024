"""
Tests the operands module & its functions
"""
import pytest
from operands.operands import add, subtract, multiply, divide

def test_add():
    """
    Test the add function
    """
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(2.5, 3.5) == 6.0
    assert add(0, 0) == 0

def test_subtract():
    """
    Test the subtract function
    """
    assert subtract(5, 2) == 3
    assert subtract(-1, 1) == -2
    assert subtract(3.5, 2.5) == 1.0
    assert subtract(0, 0) == 0

def test_multiply():
    """
    Test the multiply function
    """
    assert multiply(2, 3) == 6
    assert multiply(-1, 1) == -1
    assert multiply(2.5, 3.5) == 8.75
    assert multiply(0, 0) == 0

def test_divide():
    """
    Test the divide function
    """
    assert divide(6, 3) == 2.0
    assert divide(-6, 3) == -2.0
    assert divide(10, 2) == 5.0
    assert divide(0, 5) == 0.0
    assert divide(5, 2) == 2.5
    with pytest.raises(ValueError):
        divide(4, 0)
