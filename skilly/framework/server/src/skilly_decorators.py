import json
from functools import wraps

import jwt

from skilly.framework.server.src.skilly_server import routes
from skilly.framework.utils.src.controller.skilly_response_handler import ResponseHandler

"""

# Returns the wrapper function
    # Parameters:
        path: (str) -> "/get/4"
        method: (str) -> "GET"
    # Returns:
        func: (func) -> dict
"""


def route(path, method):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)

        routes[path] = (method, wrapper)
        return wrapper

    return decorator


def requireToken(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        # Extract the token from the Authorization header
        auth_header = self.headers.get('Authorization')
        message = "Token missing"
        if auth_header and auth_header.startswith('Bearer '):
            token = auth_header.split(' ')[1]
            try:
                # Verify and decode the token
                decoded_token = jwt.decode(token, 'secret', algorithms=['HS256'])
                # Perform any additional validation or checks as needed
                # ...
                # Call the decorated function if the token is valid
                return func(self, *args, **kwargs)
            except jwt.ExpiredSignatureError:
                message = "Expired token"
            except jwt.InvalidTokenError:
                message = "Invalid token"

        return ResponseHandler(
                http=ResponseHandler.HTTP_UNAUTHORIZED,
                response={}
            ).setMessage(message).send()

    return wrapper
