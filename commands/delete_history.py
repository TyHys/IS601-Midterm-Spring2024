# pylint: disable=too-few-public-methods
"""
A command class that deletes a row from the calculator's calculation history.
"""
class Command:
    """
    Represents the delete_history command, generalized for the design pattern.
    """
    def execute(self, calculator) -> None:
        """
        Executes the command to delete a history row from the calculator's calculation history.

        This method prompts the user to specify a row to remove from the calculator's history,
        then removes that row from the dataframe storing the calculation history.

        Parameters:
        calculator (Calculator): The calculator instance containing the calculation history.

        Returns:
        str: A message indicating the success or failure of the operation.
        """
        print(calculator.calc_hist.delete_history())
        return calculator.calc_hist.delete_history()
