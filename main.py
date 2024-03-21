from calculator.calculator import Calculator
from operands.operands import add,subtract,multiply,divide

operandMap = {
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide
    }

hr = "_" * 40

calcInst = Calculator()

print(f"""
  -------Valid Inputs-------
      Commands:
          ▶`get history`
          ▶`exit`
      Operations:
          ▶ `5 + 2`
          ▶ `10 / 2`
          ▶ `3 - 1`
          ▶ `10 * 5`

{hr}""")
while True:
  #Take in user input

  userIn = input("Enter your command\n")
  print(">> " + userIn)

  #Check if exit
  if userIn.lower() == 'exit':
    print("Exit command received; ending application")
    break

  #Check if history request
  elif userIn.lower() == 'get history':
    print(calcInst.calcHist.getHistory())
    print(hr)

  elif userIn.lower() == 'clear history':
    print(calcInst.calcHist.clearHistory())
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

    except:
      raise ValueError("Invalid operation received")

    result = calcInst.performOperation(operandFunc,x,y)
    print("Result :",result)
    print(hr)