class Command:
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
        print(calculator.calcHist.delete_history())
        return None