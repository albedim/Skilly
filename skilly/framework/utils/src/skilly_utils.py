from typing import Any

from skilly.package import package
from skilly.framework.utils.src.error.errors import NotFoundError


'''
# Returns an object or list of objects or null
    # Parameters:
        Class (str): class name to create the object
        isList (bool): 
        o (any): object or list of objects
    # Returns:
        object (any): Entity object
        list of objects (list[any]): List of entity objects
'''


def toObj(Class, isList, o) -> list[Any] | None | Any:
    import importlib
    if isList:
        array = []
        for e in o:
            module = importlib.import_module(package['project_name'] + '.model.repository.' + Class.lower() + "_repository")
            class_ = getattr(module, Class)
            array.append(class_(obj=e))
        return array
    else:
        try:
            if o is None:
                raise NotFoundError("This query did not return anything")
            module = importlib.import_module(package['project_name'] + 'model.repository.' + Class.lower() + "_repository")
            class_ = getattr(module, Class)
            return class_(obj=o)
        except NotFoundError as e:
            return None
