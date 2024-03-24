"""
Unit test for the clear_history command.
"""
from unittest.mock import MagicMock
import pytest
from commands.clear_history import Command
from calculator.calculator import Calculator

@pytest.fixture(name="calculator")
def fixture_calculator():
    """
    Returns a Calculator object.
    """
    return Calculator()

def test_execute_clears_history(calculator):
    """
    Test that the execute method clears the history.
    """
    # Setup
    calculator.calc_hist.clear_history = MagicMock(return_value=None)
    command = Command()

    # Action
    command.execute(calculator)

    # Assertion
    calculator.calc_hist.clear_history.assert_called_once()

def test_execute_with_non_mocked_calculator():
    """
    Test that the execute method executes without errors
    when a real Calculator object is used.
    """
    calculator = Calculator()  # Instantiate a real Calculator object
    command = Command()

    # Action & Assertion
    command.execute(calculator)  # This should not raise any errors
