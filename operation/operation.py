"""
Defines how operations should be executed within the Calculator
"""
from typing import Union, Callable

class Operation:
    """
    Defines how operations should be executed within the Calculator
    """
    def __init__(self):
        self.x_ = None
        self.y_ = None
        self.operation_ = None


    def perform_operation(
        self,
        operation: Callable,
        x: Union[int, float],
        y: Union[int, float]
    ) -> Union[int, float, None]:
        """
        Perform the operation on two operands
        """
        self.x_ = x
        self.y_ = y
        self.operation_ = operation

        return operation(x, y)

    def get_last_operation_attempt(self) -> str:
        """
        Get the last operation attempted
        """
        return f"{self.x_} {self.operation_.__name__} {self.y_}"
