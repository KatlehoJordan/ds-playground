"""
This file is meant to guide you through the main uses of python
features in VS Code.
"""

# Read-execute-print-loop (REPL) in ipython ####

# Start by using shift + enter to run code through ipython.
# If ipython does not open when starting the REPL, it could be due to:
# The wrong version of python extensions
# Incorrect configuration of .vscode/settings.json

print("hello from python")

# Pylance features ####

# Most of the features that make VS Code work with python come from pylance.
# These include: docstrings, signature help, parameter suggestions, code
# completion, auto-imports, as-you-type reporting of diagnostics, code outline
# code navigation, type-checking mode, IntelliCode compatibility, Jupyter
# Notebooks compatibility, semantic highlighting.

## autoDocstring ####

# When you define a function, autoDocstring will help populate it


def simple_demo_function(arg_1: int, arg_2: int):
    """This is a simple demo of autoDocstring

    Args:
        arg_1 (float): a number to be added
        arg_2 (float): a number to be added
    """
    return sum(range(arg_1, arg_2))


## IntelliCode ####

# Start typing a function to see tooltip with the function signature

print("Demo with intellicode")

## IntelliCode API Usage Examples

# Hover over a function in order to get a tooltip to see examples from github

sum(range(4))

# Formatting configurations ####

## Black Formatter ####

# The BlackFormatter formats on type, paste, and save based on settings.json

## isort ####

# Sorts imports automatically on type, paste, and save based on settings.json

## Pylint ####

# Linter automatically lints files as you work on them to help you catch
# and correct bad practices.

# Debugging ####

## Debug Python: Current File will pause at errors in the current file ####

# Launch debugger with F5
# Place breakpoints with F9
# Add items to the watch list to observe them at different points


def function_1(i: int):
    """Takes the i - 1 index from the list of numbers from 1 to 10

    Args:
        i (int): an integer in 1 to 10 inclusive
    """
    return list(range(1, 11))[i - 1]


inputs = [4, 5, 2, 9, 0, 8, "1"]

for x in inputs:
    function_1(x)
    # Use `# type: ignore` to silence linting errors on specific lines
    function_1(x)  # type: ignore


## Alternative Debug Python configurations ####

# One can add more configurations to .vscode/launch.json
# for initiating the debugger in a specific file, function, module,
# or other options. However it will require more configuration.

# Configure tests ####

# Navigate to tests/test_add_numbers for instructions

# Jupyter Notebook ####

# Open notebooks/data_science_quickstarts/quickstart.ipynb
