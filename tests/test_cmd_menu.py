"""
Unit test for the menu command
"""
from unittest.mock import MagicMock
from commands.menu import Command

def test_execute_returns_sorted_commands():
    """
    Test that the execute method returns the expected value.
    """
    calculator = MagicMock()
    command = Command()
    expected_commands = ['clear_history', 'delete_history', 'exit_calc', 'export_history',
                          'get_history', 'import_history', 'menu']
    actual_commands = command.execute(calculator)
    actual_commands.sort()
    assert actual_commands == expected_commands
