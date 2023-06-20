"""
This is the main entrypoint.
"""

from src.add_numbers import add_numbers


def greet(name):
    """
    This function just does an addition and gives a greeting.

    Args:
        name (str): The name of the person to be greeted.
    """
    message = f"Hello, {name}!"
    print(message)
    print("Welcome to our program!")
    print("Now we will add two numbers")
    print("We shall add 1 and 2")
    print(add_numbers(1, 2))


greet("user")
