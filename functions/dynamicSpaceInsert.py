import re
def dynamicSpaceInsert(strIn: str) -> str:
    """
    Inserts spaces around arithmetic operators (+, -, *, /) in a given string.

    Args:
    - strIn (str): The input string containing arithmetic expressions.

    Returns:
    - str: The input string with spaces inserted around arithmetic operators.

    Example:
    >>> dynamicSpaceInsert("5+3*2-6/3")
    '5 + 3 * 2 - 6 / 3'
    """
    pattern = r'(\d+)([\+\-\*/])(\d+)'
    replacement = r'\1 \2 \3'
    strIn = re.sub(pattern, replacement, strIn)
    return strIn