from logging import config
import logging

from logging_config import LOGGING_CONFIG

config.dictConfig(LOGGING_CONFIG)

logger = logging.getLogger(__name__)

def main():
    logger.debug("debug message")
    logger.info("info message")
    logger.warning("warning message")
    logger.error("error message")
    logger.critical("critical message")

if __name__ == "__main__":
    main()