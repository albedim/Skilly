from typing import Any

import jwt

from skilly.framework.utils.src.error.errors import NotFoundError, UnmappableQueryResult

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
    try:
        if isList:
            array = []
            for e in o:
                module = importlib.import_module('src.model.entity.' + Class.lower() + "_entity")
                class_ = getattr(module, Class)
                array.append(class_(obj=e))
            return array
        else:
            try:
                if o is None:
                    raise NotFoundError()
                module = importlib.import_module('src.model.entity.' + Class.lower() + "_entity")
                class_ = getattr(module, Class)
                return class_(obj=o)
            except NotFoundError as e:
                print(e)
                return None
    except UnmappableQueryResult() as e:
        print(e)
        return None


class Attr:

    def __init__(self, attribute):
        self.attribute = attribute

'''
# Returns true / false depending on the given schema. Which needs to respect the registered schema
    # Parameters:
        given_schema (dict): { "name": "Ok" }
        schemaName (str): "CREATION"
    # Returns:
        boolean
'''


def isValid(givenSchema, schemaName):
    import importlib.util
    file_path = "./schema.py"
    module_name = file_path.replace("/", ".")
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    for schema in module.SCHEMA:
        if schema['name'] == schemaName:
            for key in schema['schema']:
                if key not in givenSchema or type(givenSchema[key]) != schema['schema'][key]:
                    return False
    return True


def generateJwt(o):
    return jwt.encode(o, 'secret', algorithm='HS256')