"""
This module provides functions for making loggers.
"""

import logging
from typing import Callable


def make_logger(
    name: str = "numpy-tutorial",
    level: str = "INFO",
) -> logging.Logger:
    """
    Makes a logger, giving it a name, and setting the logging level.

    Args:
        name (str, optional): A name for the logger. Defaults to
        "default non-root logger".
        level (str, optional): The logging level. Defaults to "INFO".

    Returns:
        logging.Logger: An object that can be used to make log messages.
    """

    logger = logging.getLogger(name)
    handler = logging.StreamHandler()
    formatter = logging.Formatter(
        fmt="%(asctime)s "
        "\n\tLogger: %(name)s "
        "Module: %(module)s "
        "Function: %(funcName)s "
        "File: %(filename)s "
        "Line: %(lineno)d"
        "\n%(levelname)s:\n%(message)s\n",
        datefmt="\n%Y-%m-%d %H:%M:%S",
    )
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(level)
    return logger


def make_printer() -> Callable[..., None]:
    """
    Makes a printer. The difference to the `print()` function is subtle;
    here, doing multi-line strings are done the same way as with a logger ---
    with \\n and quotation marks but without a comma for each line. Also,
    injecting variables into the string is the same as for with the logger ---
    use %s syntax instead of f-strings.

    Returns:
        A function for printing to the logs.
    """

    logger = logging.getLogger("printer")
    handler = logging.StreamHandler()
    formatter = logging.Formatter("%(message)s")
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel("DEBUG")
    return logger.debug
