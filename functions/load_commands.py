"""
Function for dynamically loading commands
"""
import importlib
from typing import Callable

def load_command(command_name: str) -> Callable:
    """
    Dynamically load and return the command module
    """
    plugin_dir = "commands"
    command_module = importlib.import_module(f"{plugin_dir}.{command_name}")
    return command_module.Command()
