# pylint: disable=too-few-public-methods
"""
A command class that implements the exit command.
"""
import sys
class Command:
    """
    A command class that implements the exit command.
    """
    def execute(self, calculator):
        """
        Executes the exit command, terminating the application.

        This method terminates the application when called. 
        It prints a message indicating that the exit command
        has been received and ends the execution of the program. 
        Any cleanup operations needed before termination
        should be performed before calling this method.

        Parameters:
        calculator (Calculator): Defines the calculator object
        which will have its history exported.
        """
        calculator.calc_hist.export_history()
        print("Exit command received; ending application")
        # You can perform any cleanup operations here if needed
        # For example, closing files, releasing resources, etc.
        sys.exit()  # Exit the application
