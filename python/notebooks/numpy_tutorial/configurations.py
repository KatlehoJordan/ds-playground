"""
This is the configuration file for the tutorial notebooks.
"""

import argparse

from make_logger import make_logger, make_printer

argument_parser = argparse.ArgumentParser()
logger = make_logger()
printer = make_printer()

if __name__ == '__main__':
    logger.info('Hi')
