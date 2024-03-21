from history.history import History
from operation.operation import Operation
from typing import Union, Callable

class Calculator:
    def __init__(self):
        self.calcHist = History()
        self.calcOperator = Operation()  # Create an instance of Operation

    def performOperation(self, operation: Callable, x: Union[int, float], y: Union[int, float]) -> Union[int, float, None]:
        operationResult = self.calcOperator.performOperation(operation, x, y)  # Call the method on the instance
        self.calcHist.histAppend(operation, x, y, operationResult)
        return operationResult
