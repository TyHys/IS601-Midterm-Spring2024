# pylint: disable=too-few-public-methods
"""
A command class that implements the menu command.
"""
import os

class Command:
    """
    A command class that implements the menu command.
    """

    def execute(self, calculator):
        """
        Lists available commands and operations in the commands directory.

        This method scans the commands directory for Python files (excluding special files)
        and extracts the command names. It then prints the list of available commands and examples
        of operations that can be performed using the calculator.

        Parameters:
        calculator (Calculator): The calculator instance. This parameter 
            is not used in this method but is required
        by the interface for consistency with other command classes.

        Returns:
        list: A list of available command names extracted from the files in the commands directory.
        """
        print(f"Last calculation: {calculator.x_} {calculator.operand_symbol_} {calculator.y_}")
        commands = []
        for filename in os.listdir(os.path.dirname(__file__)):
            if filename.endswith(".py") and not filename.startswith("__"):
                command_name = filename.split(".")[0]
                commands.append(command_name)
        print("-------Valid Inputs-------")
        print("Commands")
        for cmd in commands:
            print("     ❖ " + cmd)
        print("-"*25)
        print(" Operations (e.g.):")
        print("     ❖ 5 + 2")
        print("     ❖ 10 / 2")
        print("     ❖ 3 - 1")
        print("     ❖ 10 * 5")

        return commands
