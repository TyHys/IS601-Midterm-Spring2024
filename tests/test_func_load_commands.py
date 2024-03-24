"""
A unit test for the load_command function in the functions.loadCommands module.
"""
from unittest.mock import patch
import pytest
from commands import (
    clear_history,
    delete_history,
    exit_calc,
    export_history,
    get_history,
    import_history,
    menu
)
from functions.load_commands import load_command

@pytest.fixture(name = 'mock_importlib')
def fixture_mock_importlib():
    """
    A fixture that mocks the importlib.import_module function.
    """
    with patch('importlib.import_module') as mock_import_module:
        yield mock_import_module

def test_load_command(mock_importlib):
    """
    Test that the load_command function loads the correct command module.
    """
    command_modules = {
        'clear_history': clear_history,
        'delete_history': delete_history,
        'exit': exit_calc,
        'export_history': export_history,
        'get_history': get_history,
        'import_history': import_history,
        'menu': menu
    }
    for command_name, command_module in command_modules.items():
        mock_importlib.return_value = command_module
        loaded_command = load_command(command_name)
        expected_command_class = getattr(command_module, 'Command', None)
        assert isinstance(loaded_command, expected_command_class), \
       f"Loaded command '{command_name}' is not an instance of its command class"
