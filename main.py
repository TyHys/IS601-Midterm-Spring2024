from calculator.calculator import Calculator
from operands.operands import add, subtract, multiply, divide
import importlib
import os


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

command = load_command('menu')
commandList = command.execute(None)

while True:
    # Take in user input
    userIn = input("Enter your command\n")
    print(">> " + userIn)

    if userIn.lower() in commandList:
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


