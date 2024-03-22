# commands/exit.py

class Command:
    def execute(self, calculator):
        """
        Executes the exit command, ending the application
        """
        print("Exit command received; ending application")
        # You can perform any cleanup operations here if needed
        # For example, closing files, releasing resources, etc.
        import sys
        sys.exit()  # Exit the application
