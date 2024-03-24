"""
Unit tests for the import_history command.
"""
import pytest
from calculator.calculator import Calculator
from commands.import_history import Command

@pytest.fixture(name="calculator")
def fixture_calculator():
    """
    Returns a Calculator object.
    """
    return Calculator()

def test_import_history_command(capfd, calculator):
    """
    Test import_history command execution.
    """
    command = Command()
    output = command.execute(calculator)
    captured = capfd.readouterr()

    assert "successfully imported" in captured.out
    assert "successfully imported" in output
