"""
This module is simply for importing into a notebook to demonstrate how modules
work.
"""


def greeting(name: str) -> None:
    """
    Prints a greeting to the console using the name passed to it.

    Args:
        name (str): A string, presumably someone's name.
    """
    print("Hello, ", name)


person = {"name": "David", "age": 37}
