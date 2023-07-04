from skilly.framework.connect import commit, get


class Repository:

    @classmethod
    def save(cls, o):
        query = f"INSERT INTO {o.__class__.__name__.lower()} VALUES("
        for prop in o.__dict__:
            query += f"'{str(o.__dict__[prop])}' , "
        commit(query[:-2] + ")")

    @classmethod
    def update(cls, o):
        query = f"UPDATE {o.__class__.__name__.lower()} SET "
        idPassed = False
        idValue = []
        for key, value in o.__dict__.items():
            if idPassed:
                query += f"{key} = '{str(value)}' , "
            else:
                idValue = [key, value]
                idPassed = True
        commit(query[:-2] + f" WHERE {idValue[0]} = {idValue[1]}")
        return o

    @classmethod
    def joinQuery(cls, query):
        return get(query, True)
