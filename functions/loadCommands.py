import importlib
from typing import Callable

def loadCommand(command_name: Callable) -> Callable:
    """
    Dynamically load and return the command module
    """
    PLUGIN_DIR = "commands"
    command_module = importlib.import_module(f"{PLUGIN_DIR}.{command_name}")
    return command_module.Command()