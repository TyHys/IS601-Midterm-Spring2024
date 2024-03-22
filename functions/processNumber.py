from typing import Union

def processNumber (strIn: str) -> Union[int,float]:
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