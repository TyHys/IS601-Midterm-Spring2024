import re
from typing import Union, Tuple

class inputCleaner():

    def commaRemoval(self,strIn: str) -> str:
         strIn = strIn.replace(',', '')
         return strIn
    
    def removeWhitespaces(self,strIn: str) -> str:
        """
        Removes all whitespace characters from a given string.

        Args:
        - strIn (str): The input string from which whitespace characters will be removed.

        Returns:
        - str: The input string with all whitespace characters removed.

        Example:
            removeWhitespaces("Hello   World!")
        'HelloWorld!'
        """
        strIn = re.sub(r'\s+', '', strIn)
        return strIn

    def dynamicSpaceInsert(self,strIn: str) -> str:
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

    import re

    def operandStrip(self,input_string: str) -> str:
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


    def multiOperandChecker(self,inputString: str) -> bool:
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
        operands = self.operandStrip(inputString)
        operandCount = len(operands)

        # Check if any operator appears more than once
        if operandCount > 1:
                return True
        else:
            return False
        
    from typing import Union

    def convertNumber (self,strIn: str) -> Union[int,float]:
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
        
    def processInput(self, strIn: str) -> Tuple[Union[int, float], str, Union[int, float]]:
         
         if(self.multiOperandChecker(strIn)):
            raise AttributeError("You may only have one operand in your operations")
         
         strIn = self.commaRemoval(strIn)
         strIn = self.removeWhitespaces(strIn)
         strIn = self.dynamicSpaceInsert(strIn)
         listOut = strIn.split(" ")

         x = self.convertNumber(listOut[0])
         operandSymbol = listOut[1]
         y = self.convertNumber(listOut[2])

         return x, operandSymbol, y