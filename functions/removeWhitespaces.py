import re
def removeWhitespaces(strIn):
        strIn = re.sub(r'\s+', '', strIn)
        return strIn

