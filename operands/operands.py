"""
Define basic arithmetic operations
"""
from typing import Union

def add(x: Union[int, float], y: Union[int, float]) -> Union[int, float]:
    """
    Add two numbers
    """
    return x + y

def subtract(x: Union[int, float], y: Union[int, float]) -> Union[int, float]:
    """
    Subtract two numbers
    """
    return x - y

def multiply(x: Union[int, float], y: Union[int, float]) -> Union[int, float]:
    """
    Multiply two numbers"""
    return x * y

def divide(x: Union[int, float], y: Union[int, float]) -> Union[float, None]:
    """
    Divide two numbers"""
    if y == 0:
        raise ValueError("Cannot divide by zero")
    return x / y
