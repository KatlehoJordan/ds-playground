"""
This file is meant to guide you through the main uses of python
features in VS Code.
"""

# Read-execute-print-loop (REPL) in ipython ####

# Start by using shift + enter to run code through ipython.
# If ipython does not open when starting the REPL, it could be due to:
# The wrong version of python extensions
# Incorrect configuration of .vscode/settings.json

from src.add_numbers import add_numbers

# Debugging ####

## Debug Python: Current File will pause at errors in the current file ####

# Launch debugger with F5
# Place breakpoints with F9
# Add items to the watch list to observe them at different points


def function_1(i):
    """Takes the i - 1 index from the list of numbers from 1 to 10

    Args:
        i (int): an integer in 1 to 10 inclusive
    """
    return list(range(1, 11))[i - 1]


inputs = [4, 5, 2, 9, 0, 8, "1"]

for x in inputs:
    function_1(x)


## Alternative Debug Python configurations ####

# One can add more configurations to .vscode/launch.json
# for initiating the debugger in a specific file, function, module,
# or other options. However it will require more configuration.


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

    print(
        "Here, we will have a very long test string in order to trigger the \
              linters to complain and see if we can resolve any of their complaints."
    )


greet("user")
