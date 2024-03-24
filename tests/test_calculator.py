"""
A unit test for the Calculator class, 
used as the primary means of calculating and storing history together.
"""
import pytest
from calculator.calculator import Calculator

@pytest.fixture(name="calculator")
def fixture_calculator():
    """
    Create a Calculator instance for testing.
    """
    return Calculator()

def test_perform_operation_add(calculator):
    """
    Test the perform_operation method with addition.
    """
    assert calculator.perform_operation(calculator.operand_map_['+'], 2, 3) == 5

def test_perform_operation_subtract(calculator):
    """
    Test the perform_operation method with subtraction.
    """
    assert calculator.perform_operation(calculator.operand_map_['-'], 5, 3) == 2

def test_perform_operation_multiply(calculator):
    """
    Test the perform_operation method with multiplication.
    """
    assert calculator.perform_operation(calculator.operand_map_['*'], 2, 3) == 6

def test_perform_operation_divide(calculator):
    """
    Test the perform_operation method with division.
    """
    assert calculator.perform_operation(calculator.operand_map_['/'], 6, 3) == 2

def test_ingest_operation_add(calculator):
    """
    Test the ingest_operation method with addition.
    """
    assert calculator.ingest_operation("2+3") == 5

def test_ingest_operation_subtract(calculator):
    """
    Test the ingest_operation method with subtraction.
    """
    assert calculator.ingest_operation("5-3") == 2

def test_ingest_operation_multiply(calculator):
    """
    Test the ingest_operation method with multiplication.
    """
    assert calculator.ingest_operation("2*3") == 6

def test_ingest_operation_divide(calculator):
    """
    Test the ingest_operation method with division.
    """
    assert calculator.ingest_operation("6/3") == 2

def test_ingest_operation_invalid_input(calculator):
    """
    Test the ingest_operation method with invalid input.
    """
    with pytest.raises(ValueError):
        calculator.ingest_operation("2&3")

def test_ingest_operation_division_by_zero(calculator):
    """
    Test the ingest_operation method with division by zero.
    """
    with pytest.raises(ValueError):
        calculator.ingest_operation("6/0")

def test_history_append(calculator):
    """
    Test the hist_append method.
    """
    calculator.ingest_operation("2+3")
    assert calculator.calc_hist.hist_df.shape == (1,4)
    assert calculator.calc_hist.hist_df.at[0, 'result'] == 5
