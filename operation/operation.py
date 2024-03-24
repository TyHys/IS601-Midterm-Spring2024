from typing import Union, Callable

class Operation:

    def perform_operation(self, operation: Callable, x: Union[int, float], y: Union[int, float]) -> Union[int, float, None]:
        try:
            return operation(x, y)
        except NameError as e:
            print("Operand does not exist:", e)
