"""
A unit test for the export_history command.
"""
import pytest
from calculator.calculator import Calculator
from commands.export_history import Command

@pytest.fixture(name="calculator")
def fixture_calculator():
    """
    Returns a Calculator object.
    """
    return Calculator()

def test_export_history_command_prints_history(capfd, calculator):
    """
    Test that the export_history command prints the history.
    """
    # Arrange
    calculator.calc_hist.hist_append(lambda x, y: x + y, 2, 3, 5)
    calculator.calc_hist.hist_append(lambda x, y: x * y, 4, 5, 20)
    command = Command()

    # Act
    command.execute(calculator)

    # Assert
    captured = capfd.readouterr()
    assert captured.out.strip() == "History saved to history/history_export.csv"

def test_export_history_command_empty_history(calculator):
    """
    Test that the export_history command prints a message when the history is empty.
    """
    # Arrange
    command = Command()

    print(calculator.calc_hist.clear_history())
    calculator.calc_hist.clear_history()
    result = command.execute(calculator)


    assert result == "No history"
