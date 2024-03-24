# pylint: disable=too-few-public-methods

"""
Command to clear the history of the calculator instance.
"""
class Command:
    """
    Represents the clear_history command, generalized for the design pattern.
    """
    def execute(self, calculator) -> None:
        """
        Executes the command to clear the history of the calculator instance.

        This method removes all history records stored in the calculator instance,
        effectively clearing the history of previous calculations.

        Parameters:
        calculator (Calculator): The calculator instance whose history is to be cleared.
        """
        print(calculator.calc_hist.clear_history())
