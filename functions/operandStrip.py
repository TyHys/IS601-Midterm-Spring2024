import re

def operandStrip(input_string: str) -> str:
    """
    Removes all characters from a string except "+", "*", "/", and "-".

    Args:
    - input_string (str): The input string to filter characters.

    Returns:
    - str: The modified string containing only the specified characters.

    Example:
    >>> keep_specific_characters("5 * 5 + 5")
    '*+'
    """
    # Define the pattern to match characters other than "+", "*", "/", and "-"
    pattern = r'[^+\-*/]'

    # Remove all characters except the specified ones
    filtered_string = re.sub(pattern, '', input_string)

    return filtered_string
