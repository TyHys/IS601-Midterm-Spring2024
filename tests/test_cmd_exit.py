# pylint: disable=too-few-public-methods
"""
Unit test for the exit command
"""
from unittest.mock import MagicMock
import pytest
from commands.exit_calc import Command

class TestCommand:
    """
    TestCommand class for the exit command
    """
    def test_execute(self):
        """
        Test that the execute method returns the expected value.
        """
        calculator = MagicMock()
        calculator.calc_hist = MagicMock()

        command = Command()
        with pytest.raises(SystemExit) as pytest_wrapped_e:
            command.execute(calculator)

        assert pytest_wrapped_e.type == SystemExit
        assert pytest_wrapped_e.value.code is None
