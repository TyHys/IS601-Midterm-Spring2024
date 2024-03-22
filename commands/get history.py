# commands/get_history_command.py

class Command:
    def execute(self, calculator):
        """
        Executes the get_history command, printing the calculation history
        """
        print(calculator.calcHist.getHistory())