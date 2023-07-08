"""
This module is a simplified way to do tests with pytest.

To configure tests, launch the command palette.

Tests should then be executable and debuggable from the VS Code icons in the
lefthand side bar.
"""

from src.add_numbers import add_numbers


def test_add_numbers():
    """
    This tests the add_numbers function.
    """
    result = add_numbers(2, 3)
    assert result == 5
