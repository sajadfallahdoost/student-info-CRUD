import logging


def setup_logger() -> logging.Logger:
    """Sets up a logger for the application."""
    logger = logging.getLogger("StudentCRUD")
    logger.setLevel(logging.DEBUG)
    handler = logging.StreamHandler()
    handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
    logger.addHandler(handler)
    return logger
