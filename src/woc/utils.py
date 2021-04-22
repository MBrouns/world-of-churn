from functools import wraps
import datetime as dt
import logging
import sys

def log_debug(func):
    @wraps(func)
    def wrapper(*args, **kwargs):

        logger = logging.getLogger(sys.modules[func.__module__].__name__)

        tic = dt.datetime.now()
        result = func(*args, **kwargs)
        time_taken = str(dt.datetime.now() - tic)
        logger.debug(f"[{func.__name__}] shape={result.shape} time={time_taken}")
        return result
    return wrapper

def log_info(func):
    @wraps(func)
    def wrapper(*args, **kwargs):

        logger = logging.getLogger(sys.modules[func.__module__].__name__)

        tic = dt.datetime.now()
        result = func(*args, **kwargs)
        time_taken = str(dt.datetime.now() - tic)
        logger.info(f"[{func.__name__}] shape={result.shape} time={time_taken}")
        return result
    return wrapper
