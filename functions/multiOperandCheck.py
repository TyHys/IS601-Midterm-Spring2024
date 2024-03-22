import re

def multiOperandChecker(input_string: str) -> bool:
    # Define the pattern to match the operators
    pattern = r'[\+\-\*/]'

    # Find all occurrences of the operators in the input string
    operators = re.findall(pattern, input_string)

    # Count the number of occurrences
    operator_counts = {operator: operators.count(operator) for operator in set(operators)}

    # Check if any operator appears more than once
    for count in operator_counts.values():
        if count > 1:
            return True
    
    return False