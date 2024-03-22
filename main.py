from calculator.calculator import Calculator
from operands.operands import add, subtract, multiply, divide
import importlib
import os

print('hello world')

operandMap = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

hr = "_" * 30

calcInst = Calculator()

PLUGIN_DIR = "commands"


def load_command(command_name):
    """
    Dynamically load and return the command module
    """
    command_module = importlib.import_module(f"{PLUGIN_DIR}.{command_name}")
    return command_module.Command()


def list_commands():
    """
    List available commands in the commands directory
    """
    commands = []
    for filename in os.listdir(PLUGIN_DIR):
        if filename.endswith(".py") and not filename.startswith("__"):
            command_name = filename.split(".")[0]
            commands.append(command_name)
    return commands

print("-------Valid Inputs-------")
print(" Commands")
for cmd in list_commands():
      print('     ❖',cmd)
print("-"*25)
print(" Operations")
print(" Examples:")
print("     ❖ 5 + 2")
print("     ❖ 10 / 2")
print("     ❖ 3 - 1")
print("     ❖ 10 * 5")
print(hr)

while True:
    # Take in user input
    userIn = input("Enter your command\n")
    print(">> " + userIn)

    if userIn.lower() in list_commands():
        command = load_command(userIn)
        command.execute(calcInst)
        print(hr)

    else:
        try:
            userIn = userIn.split(" ")

            x = userIn[0]
            x = float(x)

            operandSymbol = userIn[1]
            operandFunc = operandMap[operandSymbol]

            y = userIn[2]
            y = float(y)

            result = calcInst.performOperation(operandFunc, x, y)
            print("Result:", result)
            print(hr)

        except:
            raise ValueError("Invalid operation received")


