"""
Tests for the input cleaner class used within the calculator.
"""

import pytest
from input_cleaner.input_cleaner import InputCleaner

# Instantiate inputCleaner class
cleaner = InputCleaner()


# Test comma_removal function
def test_comma_removal():
    """
    Test the comma_removal function in the input_cleaner.py file.
    """
    assert cleaner.comma_removal("1,000,000") == "1000000"
    assert cleaner.comma_removal("1,000,000.00") == "1000000.00"
    assert cleaner.comma_removal("10,000") == "10000"

# Test removeWhitespaces function
def test_remove_whitespaces():
    """
    Test the remove_whitespaces function in the input_cleaner.py file.
    """
    assert cleaner.remove_whitespaces("Hello   World!") == "HelloWorld!"
    assert cleaner.remove_whitespaces("   This  is   a   test   ") == "Thisisatest"
    assert cleaner.remove_whitespaces("NoSpacesHere") == "NoSpacesHere"

# Test dynamicSpaceInsert function
def test_dynamic_space_insert():
    """
    Test the dynamic_space_insert function in the input_cleaner.py file.
    """
    assert cleaner.dynamic_space_insert("5+3*2-6/3") == "5 + 3 * 2 - 6 / 3"
    assert cleaner.dynamic_space_insert("10-2/5+7") == "10 - 2 / 5 + 7"
    assert cleaner.dynamic_space_insert("2*4-7+9/3") == "2 * 4 - 7 + 9 / 3"

# Test operandStrip function
def test_operand_strip():
    """
    Test the operand_strip function in the input_cleaner.py file.
    """
    assert cleaner.operand_strip("5 * 5 + 5") == "*+"
    assert cleaner.operand_strip("10 - 2 / 5") == "-/"
    assert cleaner.operand_strip("2 * 4 - 7 + 9 / 3") == "*-+/"

# Test multiOperandChecker function
def test_multi_operand_checker():
    """
    Test the multi_operand_checker function in the input_cleaner.py file."""
    assert cleaner.multi_operand_checker("5 * 5 + 5") is True
    assert cleaner.multi_operand_checker("10 - 2 / 5") is True
    assert cleaner.multi_operand_checker("2 * 4 - 7 + 9 / 3") is True
    assert cleaner.multi_operand_checker("5 + 3") is False


def test_convert_number_float_error():
    """
    Test the convert_number function in the input_cleaner.py file.
    """
    with pytest.raises(ValueError):
        cleaner.convert_number("a.bc")

# Test convert_number function
def test_convert_number_int_error():
    """
    Test the convert_number function in the input_cleaner.py file.
    """
    with pytest.raises(ValueError):
        cleaner.convert_number("abc")

# Test convert_number function
def test_convert_number_success():
    """
    Test the convert_number function in the input_cleaner.py file.
    """
    assert cleaner.convert_number("5.5") == 5.5

# Test processInput function
def test_process_input():
    """
    Test the process_input function in the input_cleaner.py file.
    """
    assert cleaner.process_input("5 * 5") == (5, "*", 5)
    assert cleaner.process_input("10 - 2") == (10, "-", 2)
    assert cleaner.process_input("2 * 4") == (2, "*", 4)
    assert cleaner.process_input("9 / 3") == (9, "/", 3)
