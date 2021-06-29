from application.share.utils import print_all, stdout
from functools import wraps
from flask import request


class security:
    def user_auth(self, func):
        wraps(func)

        def decorator(*args, **kwargs):
            return func(*args, **kwargs)

        decorator.__name__ = func.__name__
        return decorator


secure = security()
