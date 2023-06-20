import json

from skilly.framework.skilly_repository import createQuery


def my_decorator(func):
    def wrapper(*pargs, **kwargs):
        print(pargs[0], kwargs)

    return wrapper


def Entity(func):
    tables = json.load(open("tables.json"))
    query = f"CREATE TABLE {func.__name__} ("
    for param in func.__dict__:
        if param != '__module__' and param != '__dict__' and param != '__weakref__' and param != '__doc__' and param != '__init__':
            query += f"{param} {func.__dict__[param]}"
    tables.append({
        "name": func.__name__,
        "query": query[:-1] + ")"
    })
    with open("tables.json", "w") as outline:
        json.dump(tables, outline)


def autoQBN(func):
    def wrapper(*pargs, **kwargs):
        return createQuery(func, *pargs[1:])
    return wrapper


def manualQBN(query):
    def wrapper():
        return query
    return wrapper


class Skilly:

    def __init__(self, *params):
        for param in params:
            Entity(param)

