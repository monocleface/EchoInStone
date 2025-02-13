import time
import logging

logger = logging.getLogger(__name__)

def log_time(message):
    """Logs the current time with a given message."""
    logger.debug(f"{message}: {time.time()}")

def timer(func):
    """Decorator to measure the execution time of a function."""
    def wrapper(*args, **kwargs):
        start_time = time.time()
        logger.debug(f"Starting {func.__name__}...")
        result = func(*args, **kwargs)
        end_time = time.time()
        elapsed_time = end_time - start_time
        logger.debug(f"{func.__name__} took {elapsed_time:.4f} seconds to execute.")
        return result
    return wrapper
