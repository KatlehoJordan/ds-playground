"""
This module is a simplified way to do tests with pytest.
"""

from src.add_numbers import add_numbers


def test_add_numbers():
    """
    This tests the add_numbers function.
    """
    result = add_numbers(2, 3)
    assert result == 5
