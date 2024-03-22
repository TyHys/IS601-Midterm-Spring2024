class Command:
    def execute(self, calculator) -> None:
        """
        Executes the command to clear the history of the calculator instance.

        This method removes all history records stored in the calculator instance,
        effectively clearing the history of previous calculations.

        Parameters:
        calculator (Calculator): The calculator instance whose history is to be cleared.
        """
        print(calculator.calcHist.clearHistory())
        return None