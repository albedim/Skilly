from skilly.framework.db.src.init.skilly_connect import commit


def entityInit(*func):
    for entity in func:
        query = f"CREATE TABLE IF NOT EXISTS {entity.__name__} ("
        for param in entity.__dict__:
            if param != '__module__' and param != '__dict__' and param != '__weakref__' and param != '__doc__' and param != '__init__':
                query += f"{param} {entity.__dict__[param]}"
        print("[skilly.entity] -> entity '"+entity.__name__+"' was created/checked")
        commit(query[:-1] + ")")