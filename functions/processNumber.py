from typing import Union

def processNumber (strIn: str) -> Union[int,float]:
    """
    Convert a string representation of a number to either an integer or a float.

    Args:
    - strIn (str): The input string representation of a number.

    Returns:
    - Union[int, float]: The converted number as an integer if possible, otherwise as a float.

    Raises:
    - ValueError: If the input string is not a valid number.

    Example:
    >>> processNumber("5")
    5
    >>> processNumber("3.14")
    3.14
    """
    if '.' in strIn:
        try:
            strIn = float(strIn)
        except:
            raise ValueError("Invalid number received")
    else:
        try:
            strIn = int(strIn)
        except:
            raise ValueError("Invalid number received")
    
    return strIn