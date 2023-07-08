from typing import Callable, Any
from skilly.framework.db.src.model.orm.skilly_sql_orm import createQuery
from skilly.framework.utils.src.controller.skilly_response_handler import ResponseHandler
from skilly.framework.utils.src.skilly_utils import isValid

'''
# Returns the wrapper function, which returns an object coming from createQuery method
    # Parameters:
        func (func): function
    # Returns:
        object (any): Entity object
'''


def autoQBN(func) -> \
        Callable[[tuple[Any, ...], dict[str, Any]], Any]:
    def wrapper(*pargs, **kwargs):
        return createQuery(func, *pargs[1:])

    return wrapper


'''
# Returns the wrapper function, which returns null
    # Parameters:
        func (func): function
    # Returns:
        -
'''


def entity(func) -> \
        Callable[[tuple[Any, ...], dict[str, Any]], None]:
    def wrapper(*pwargs, **kwargs):
        o = pwargs[0]
        counter = 0
        if len(kwargs) > 0:
            for param in o.__class__.__dict__:
                if param != '__module__' \
                        and param != '__dict__' \
                        and param != '__weakref__' \
                        and param != '__doc__' \
                        and param != '__init__':
                    setattr(o, param, kwargs['obj'][counter])
                    counter += 1
        else:
            for param in o.__class__.__dict__:
                if param != '__module__' \
                        and param != '__dict__' \
                        and param != '__weakref__' \
                        and param != '__doc__' \
                        and param != '__init__':
                    setattr(o, param, pwargs[counter])
                    counter += 1

    return wrapper


'''
# Returns the wrapper function, which returns what the base function returns
    # Parameters:
        schema_name (str): "CREATION"
    # Returns:
        func(schemaName, body)
        Response(400)
'''


def schema(schema_name):
    def decorator(func):
        def wrapper(cls, body):
            if not isValid(body, schema_name):
                return ResponseHandler.send().BAD_REQUEST()
            return func(cls, body)
        return wrapper

    return decorator
