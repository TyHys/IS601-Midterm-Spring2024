import re
def removeWhitespaces(strIn: str) -> str:
        strIn = re.sub(r'\s+', '', strIn)
        return strIn

