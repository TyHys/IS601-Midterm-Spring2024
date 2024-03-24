"""
Provides a class for taking in user input and 
    performing operations on it after cleaning.
    Also provides a means of viewing the inputs, 
    exporting/importing/clearing/deleting them as well.
"""

from typing import Union, Callable
from history.history import History
from operation.operation import Operation
from input_cleaner.input_cleaner import InputCleaner
from operands.operands import add,subtract,multiply,divide

class Calculator:
    """
    Calculator class which will take in user input, 
        and perform calculations on it.
    """
    def __init__(self):
        self.calc_hist = History()
        self.calc_operator = Operation()
        self.calc_cleaner = InputCleaner()
        self.operand_map_ = {'+':add,'-':subtract,'*':multiply,'/':divide}
        self.x_ = None
        self.y_ = None
        self.operand_symbol_ = None

    def perform_operation(
            self,
            operation: Callable,
            x: Union[int, float],
            y: Union[int, float]
            ) -> Union[int, float, None]:
        """
        Perform an operation on two numbers.
        """
        operation_result = self.calc_operator.perform_operation(operation, x, y)
        self.calc_hist.hist_append(operation, x, y, operation_result)
        return operation_result

    def ingest_operation(self,str_in):
        """
        Take in a str_ing, clean it, and perform an operation on it.
        """
        x, operand_symbol, y =self.calc_cleaner.process_input(str_in)

        self.x_ = x
        self.y_ = y
        self.operand_symbol_ = operand_symbol
        return self.perform_operation(self.operand_map_[operand_symbol],x,y)
