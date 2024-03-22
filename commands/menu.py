import os

class Command:

    def execute(self, calculator):
        """
        List available commands in the commands directory
        """
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
