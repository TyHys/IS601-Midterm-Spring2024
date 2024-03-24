"""
A unit test for the execute method in the Command class of the menu command.
"""
import os
import pytest
from commands.menu import Command
from calculator.calculator import Calculator

@pytest.fixture(name="command_instance")
def fixture_command_instance():
    """
    Provides a new Command instance for each test.
    """
    return Command()

@pytest.fixture(name="calc_instance")
def fixture_calc_instance():
    """
    Provides a new Command instance for each test.
    """
    return Calculator()

def test_execute(calc_instance,command_instance, tmp_path, capsys):
    """
    Tests the execute method of the Command class in the menu command.
    """
    # Create temporary Python files for the commands
    commands = ["clear_history", "get_history", "export_history",
                 "import_history", "menu", "exit", "delete_history"]
    for cmd in commands:
        with open(os.path.join(tmp_path, f"{cmd}.py"), "w", encoding="utf-8") as f:
            f.write("")

    # Execute the method
    result = command_instance.execute(calc_instance)

    # Sort both lists for comparison
    result.sort()
    expected_commands = sorted(commands)

    # Check if the result matches the expected commands
    assert result == expected_commands

    # Check if only the expected commands are printed
    captured = capsys.readouterr()
    for cmd in expected_commands:
        assert cmd in captured.out

    # Check if there are no additional commands printed
    for cmd in commands:
        assert cmd in captured.out
