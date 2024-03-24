"""
A module for cleaning input strings for arithmetic operations.
"""
import re
from typing import Union, Tuple

class InputCleaner:
    """
    A class that cleans input strings for arithmetic operations.
    """

    def comma_removal(self, str_in: str) -> str:
        """
        Remove commas from the input string.

        Args:
        - str_in (str): The input string possibly containing commas.

        Returns:
        - str: The input string with commas removed.

        Example:
        >>> cleaner = InputCleaner()
        >>> cleaner.comma_removal("1,000,000")
        '1000000'
        >>> cleaner.comma_removal("1,000,000.00")
        '1000000.00'
        >>> cleaner.comma_removal("10,000")
        '10000'
        """
        return str_in.replace(',', '')

    def remove_whitespaces(self, str_in: str) -> str:
        """
        Removes all whitespace characters from a given string.

        Args:
        - str_in (str): The input string from which whitespace characters will be removed.

        Returns:
        - str: The input string with all whitespace characters removed.

        Example:
            remove_whitespaces("Hello   World!")
        'HelloWorld!'
        """
        return re.sub(r'\s+', '', str_in)

    def dynamic_space_insert(self, str_in: str) -> str:
        """
        Inserts spaces around arithmetic operators (+, -, *, /) in a given string.

        Args:
        - str_in (str): The input string containing arithmetic expressions.

        Returns:
        - str: The input string with spaces inserted around arithmetic operators.

        Example:
        >>> InputCleaner().dynamic_space_insert("5+3*2-6/3")
        '5 + 3 * 2 - 6 / 3'
        """
        pattern = r'([\+\-\*/])'
        return re.sub(pattern, r' \1 ', str_in)

    def operand_strip(self, input_string: str) -> str:
        """
        Removes all characters from a string except "+", "*", "/", and "-".

        Args:
        - input_string (str): The input string to filter characters.

        Returns:
        - str: The modified string containing only the specified characters.

        Example:
        >>> InputCleaner().operand_strip("5 * 5 + 5")
        '*+'
        """
        pattern = r'[^+\-*/]'
        return re.sub(pattern, '', input_string)

    def multi_operand_checker(self, input_string: str) -> bool:
        """
        Checks if there are multiple arithmetic operators in the input string.

        Args:
        - input_string (str): The input string to check for multiple operators.

        Returns:
        - bool: True if multiple operators are found, False otherwise.

        Example:
        >>> InputCleaner().multi_operand_checker("5 * 5 + 5")
        True
        """
        operands = self.operand_strip(input_string)
        return len(operands) > 1


    def convert_number(self, str_in: str) -> Union[int, float]:
        """
        Convert a string representation of a number to either an integer or a float.

        Args:
        - str_in (str): The input string representation of a number.

        Returns:
        - Union[int, float]: The converted number as an integer if possible, otherwise as a float.

        Raises:
        - ValueError: If the input string is not a valid number.

        Example:
        >>> InputCleaner().convert_number("5")
        5
        >>> InputCleaner().convert_number("3.14")
        3.14
        """
        try:
            return int(str_in)
        except ValueError:
            try:
                return float(str_in)
            except ValueError as exc:
                raise ValueError("Invalid number received") from exc


    def process_input(self, str_in: str) -> Tuple[Union[int, float], str, Union[int, float]]:
        """
        Processes the input string for arithmetic operations.

        Args:
        - str_in (str): The input string containing an arithmetic expression.

        Returns:
        - Tuple[Union[int, float], str, Union[int, float]]: 
                A tuple containing the operands and operator.

        Raises:
        - AttributeError: If there are multiple operands in the input string.
        """
        if self.multi_operand_checker(str_in):
            raise AttributeError("You may only have one operand in your operations")

        str_in = self.comma_removal(str_in)
        str_in = self.remove_whitespaces(str_in)
        str_in = self.dynamic_space_insert(str_in)
        list_out = str_in.split(" ")

        x = self.convert_number(list_out[0])
        operand_symbol = list_out[1]
        y = self.convert_number(list_out[2])

        return x, operand_symbol, y
