"""
A unit test for the get_history command.
"""
import pytest
from commands.get_history import Command
from calculator.calculator import Calculator

@pytest.fixture(name="calculator")
def fixture_calculator():
    """
    Returns a Calculator object.
    """
    return Calculator()

def test_execute_prints_history(calculator):
    """
    Test that the get_history command prints the history.
    """
    calculator.calc_hist.hist_append(lambda x, y: x + y, 2, 3, 5)
    calculator.calc_hist.hist_append(lambda x, y: x * y, 4, 5, 20)
    command = Command()

    my_hist = command.execute(calculator)

    assert my_hist.shape == (2,4)

def test_execute_empty_history(capfd, calculator):
    """
    Test that the get_history command prints a message when the history is empty.
    """
    command = Command()

    # Act
    command.execute(calculator)

    # Assert
    captured = capfd.readouterr()
    assert captured.out.strip() == "No history"
