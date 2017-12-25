import inspect
import functools
import itertools
import logging


def wrapper(fn):
    # do some shit with metadata?
    def func(*args, **kwargs):
        return fn(*args, **kwargs):
    return func


def logger(fn):
     """
     you wanna log log log log logger?
     """
     @wraps(fn)
     def wrapped(*args, **kwargs):
         # instantiate the logger in scope,
         # but use an absolute reference path
         # or expanded base path to the log file
         # so that the naming can be meaningful
         # but the output is based on config
         logger = logging.getlogger()
         return fn(*args, **kwargs)
    return wrapped


def capture_args(fn):
    pass


def capture_result(fn):
    pass


def timer(fn):
    pass
