"""
Unit tests for the Operation class
"""
import pytest
from operation.operation import Operation

@pytest.fixture(name="operation_instance")
def fixture_operation_instance():
    """
    Create an Operation instance for testing.
    """
    return Operation()

def test_get_last_operation_attempt(operation_instance):
    """
    Test the get_last_operation_attempt method of the Operation class
    """

    result = operation_instance.perform_operation(lambda x, y: x + y, 2, 3)
    assert result == 5

    last_operation_attempt = operation_instance.get_last_operation_attempt()
    assert last_operation_attempt == "2 <lambda> 3"
