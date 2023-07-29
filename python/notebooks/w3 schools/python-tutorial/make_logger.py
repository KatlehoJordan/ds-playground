"""
This module makes a logger.
"""

import logging


def make_logger(
    name: str = "default non-root logger",
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
        "%(name)s "
        "logged a message"
        "\n\n%(levelname)s:\n"
        "%(message)s"
        "\n\t\tModule: %(module)s"
        "\tFunction: %(funcName)s"
        "\n\t\tFile: %(filename)s "
        "\tLine: %(lineno)d",
        datefmt="On %Y-%m-%d at %H:%M:%S",
    )
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(level)
    return logger
