"""
This file is meant to be run from a non-interactive session to show
how the logger configuration works.
To see this in action, run python logging_demo.py from a terminal.
"""

from configurations import argument_parser
from make_logger import make_logger


def log_messages(name: str, level: str) -> None:
    """
    Logs messages based on the logging level., first creating a logger based on the level,
    then logging the messages

    Args:
        name (str): _description_
        level (str): _description_
    """
    logger = make_logger(name=name, level=level)
    prefix_message = "Threshold low enough for"
    suffix_message = "messages"
    possible_levels = ["debug", "info", "warning", "error", "critical"]
    for possibility in possible_levels:
        getattr(logger, possibility)(
            "%s %s %s", prefix_message, possibility, suffix_message
        )


def main() -> None:
    """
    Calling this file from the command line will run this function.
    This function accepts an optional -l or --level flag from the command line
    to specify the level of logging to use.
    The function then calls the log_messages function in order to log messages
    based on the level that was passed to it.
    The function also names a logger based on the level.
    """
    argument_parser.add_argument(
        "-l",
        "--level",
        type=str,
        help="The logging level. Defaults to INFO",
        choices=["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"],
        default="INFO",
        required=False,
    )
    arguments = argument_parser.parse_args()

    logger_name = f"{arguments.level.lower()}_logger"
    log_messages(name=logger_name, level=arguments.level)


if __name__ == "__main__":
    main()
