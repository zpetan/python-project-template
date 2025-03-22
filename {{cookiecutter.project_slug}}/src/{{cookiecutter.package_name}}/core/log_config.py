"""Logging module."""

import logging
import logging.config

__all__ = ["get_logger"]


def get_logger(name: str) -> logging.Logger:
    """Generates a logger.

    Args:
        name (str): e.g. __name__

    Returns:
        logging.Logger: Logger according to below configuration.
    """
    # Use with logging.config.dictConfig
    log_config = {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "default": {
                "format": "%(asctime)s - %(levelname)s - %(message)s",
                "datefmt": "%Y-%m-%d %H:%M:%S",
            }
        },
        "handlers": {
            "stdout": {
                "class": "logging.StreamHandler",
                "formatter": "default",
                "stream": "ext://sys.stdout",
            }
        },
        "loggers": {"": {"handlers": ["stdout"], "level": "DEBUG", "propagate": True}},
    }
    logging.config.dictConfig(log_config)
    return logging.getLogger(name)
