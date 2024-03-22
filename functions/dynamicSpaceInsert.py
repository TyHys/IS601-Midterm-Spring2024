import re
def dynamicSpaceInsert(strIn):
    pattern = r'(\d+)([\+\-\*/])(\d+)'
    replacement = r'\1 \2 \3'
    strIn = re.sub(pattern, replacement, strIn)
    return strIn