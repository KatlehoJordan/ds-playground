"""
This module is simplified for building pytest against it.
"""


def add_numbers(num_a: float, num_b: float) -> float:
    """This function adds two numbers together.

    Args:
        num_a (numeric): any number
        num_b (numeric): any number

    Returns:
        numeric: The sum of a and b.
    """
    results = num_a + num_b
    return results


if __name__ == "__main__":
    print("Running add_numbers.py as entrypoint")
    print("Add 2 and 3")
    print(add_numbers(2, 3))
