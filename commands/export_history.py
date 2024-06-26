# pylint: disable=too-few-public-methods
"""
A command to export the calculation history to a file.
"""
class Command:
    """
    A command class that implements the export_history command.
    """
    def execute(self, calculator) -> None:
        """
        Executes the get_history command, printing the calculation history.

        This method retrieves the calculation history from the 
        calculator instance and prints it to the console.
        The calculation history typically includes past calculations performed using the calculator.

        Parameters:
        calculator (Calculator): The calculator instance containing the calculation history.
        """
        print(calculator.calc_hist.export_history())
        return calculator.calc_hist.export_history()
