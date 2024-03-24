"""
Unit tests for the delete_history command.
"""
from unittest.mock import MagicMock
import pytest
from commands.delete_history import Command

@pytest.fixture(name="calculator_mock")
def fixture_calculator_mock():
    """
    Returns a MagicMock object for the Calculator class.
    """
    calculator_mock = MagicMock()
    out_str = "History export file 'history/history_export.csv' deleted"
    calculator_mock.calc_hist.delete_history.return_value = out_str
    return calculator_mock

def test_execute(calculator_mock):
    """
    Test that the execute method returns the expected value.
    """
    # Create a Command instance
    command = Command()

    # Call the execute method
    result = command.execute(calculator_mock)

    # Assert that the method returned the expected value
    assert result == "History export file 'history/history_export.csv' deleted"
