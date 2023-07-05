from functools import wraps
from skilly.framework.server.src.server import routes


def route(path, method):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)

        routes[path] = (method, wrapper)
        return wrapper

    return decorator