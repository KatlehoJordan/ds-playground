"""
This is the configuration file for the tutorial notebooks.
"""

import logging

logger = logging.getLogger(__name__)
handler = logging.StreamHandler()
formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s :\n\n\t\t %(message)s\n\n"
)
handler.setFormatter(formatter)
logger.addHandler(handler)
