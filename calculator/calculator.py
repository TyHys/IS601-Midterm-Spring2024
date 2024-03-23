from history.history import History
from operation.operation import Operation
from typing import Union, Callable
from input_cleaner.input_cleaner import inputCleaner
from operands.operands import add,subtract,multiply,divide

class Calculator:
    def __init__(self):
        self.calcHist = History()
        self.calcOperator = Operation()  # Create an instance of Operation
        self.calcCleaner = inputCleaner()
        self.operandMap_ = {'+':add,'-':subtract,'*':multiply,'/':divide}
        self.x_ = None
        self.y_ = None
        self.operandSymbol_ = None
        self.lastError_ = None

    def performOperation(self, operation: Callable, x: Union[int, float], y: Union[int, float]) -> Union[int, float, None]:
        operationResult = self.calcOperator.performOperation(operation, x, y)  # Call the method on the instance
        self.calcHist.histAppend(operation, x, y, operationResult)
        return operationResult
    
    def ingestOperation(self,strIn):
        x, operandSymbol, y =self.calcCleaner.processInput(strIn)
        
        self.x_ = x
        self.y_ = y
        self.operandSymbol_ = operandSymbol
        return self.performOperation(self.operandMap_[operandSymbol],x,y)