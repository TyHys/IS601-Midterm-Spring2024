import re
def removeWhitespaces(strIn: str) -> str:
        """
        Removes all whitespace characters from a given string.

        Args:
        - strIn (str): The input string from which whitespace characters will be removed.

        Returns:
        - str: The input string with all whitespace characters removed.

        Example:
        >>> removeWhitespaces("Hello   World!")
        'HelloWorld!'
        """
        strIn = re.sub(r'\s+', '', strIn)
        return strIn

