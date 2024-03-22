import re
from functions.operandStrip import operandStrip

def multiOperandChecker(inputString: str) -> bool:
    """
    Checks if there are multiple arithmetic operators in the input string.

    Args:
    - input_string (str): The input string to check for multiple operators.

    Returns:
    - bool: True if multiple operators are found, False otherwise.

    Example:
    >>> multiOperandChecker("5 * 5 + 5")
    True
    """
    # Define the pattern to match the operators
    operands = operandStrip(inputString)
    operandCount = len(operands)

    # Check if any operator appears more than once
    if operandCount > 1:
            return True
    else:
        return False
