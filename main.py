import logging
from calculator.calculator import Calculator
from operands.operands import add, subtract, multiply, divide
from functions.multiOperandCheck import multiOperandChecker
from functions.loadCommands import loadCommand
from functions.removeWhitespaces import removeWhitespaces
from functions.dynamicSpaceInsert import dynamicSpaceInsert

# Configure logging
logging.basicConfig(filename='calculator.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logging.info("Program started")

operandMap = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

hr = "_" * 30

calcInst = Calculator()

command = loadCommand('menu')
commandList = command.execute(None)

while True:
    # Take in user input
    userIn = input("Enter your command\n")
    logging.info(f"User input: {userIn}")
    print(">> " + userIn)

    if userIn.lower() in commandList:
        logging.info(f"Command executed: {userIn}")
        command = loadCommand(userIn)
        command.execute(calcInst)        
        print(hr)

    elif multiOperandChecker(userIn):
        logging.warning("More than one operand entered into operation: %s", userIn)
        print("You may only have one operand in your operations")

    else:
        try:
            #Remove all commas
            userIn = userIn.replace(',', '')
            #Remove all whitespace characters
            userIn = removeWhitespaces(userIn)
            #Insert a whitespace character on either side of the operand
            userIn = dynamicSpaceInsert(userIn)
            #Split on the newly created spaces
            userIn = userIn.split(" ")

            x = userIn[0]
            if '.' in x:
                x = float(x)
            else:
                x = int(x)

            operandSymbol = userIn[1]
            operandFunc = operandMap[operandSymbol]

            y = userIn[2]
            if '.' in y:
                y = float(y)
            else:
                y = int(y)

            result = calcInst.performOperation(operandFunc, x, y)
            print("Result:", result)
            logging.info("Operation performed: %s %s %s = %s", x, operandSymbol, y, result)
            print(hr)

        except Exception as e:
            print("Error:", e)
            logging.error("Error occurred: %s", e)
