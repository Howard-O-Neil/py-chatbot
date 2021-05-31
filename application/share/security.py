from application.share.utils import print_all
from functools import wraps
from flask import request


class security:
    def user_auth(self, func):
        wraps(func)

        def decorator(*args, **kwargs):
            # print(f"======== request header, url: {request.path} ========")
            # print_all(request.headers)
            return func(*args)

        decorator.__name__ = func.__name__
        return decorator


secure = security()
