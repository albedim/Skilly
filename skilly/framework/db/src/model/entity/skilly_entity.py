import datetime

from skilly.framework.db.src.init.skilly_connect import commit, get, delete
from skilly.framework.utils.src.error.errors import UnmappableQueryResult, InconvertibleEntityToJSON
from skilly.framework.utils.src.skilly_utils import toObj


class Entity:

    def toJSON(self, **kvargs) -> dict:
        obj = {}
        for key in self.__dict__:
            if key != '__module__' \
                    and key != '__dict__' \
                    and key != '__weakref__' \
                    and key != '__doc__' \
                    and key != '__init__':
                obj[key] = str(self.__dict__[key]) \
                    if type(self.__dict__[key]) == datetime.datetime else self.__dict__[key]
                if type(obj[key]) != str and type(obj[key]) != int:
                    raise InconvertibleEntityToJSON(InconvertibleEntityToJSON.getMessage())
        if len(kvargs) > 0:
            for kvarg in kvargs:
                obj[kvarg] = kvargs[kvarg]
        return obj

    def save(self) -> None:
        query = f"INSERT INTO {self.__class__.__name__.lower()} VALUES("
        for prop in self.__dict__:
            query += f"'{str(self.__dict__[prop])}' , "
        commit(query[:-2] + ")")
        createdObj = toObj(self.__class__.__name__, False,
                           get("SELECT * FROM " + self.__class__.__name__ + " ORDER BY " + self.__class__.__name__.lower() + "_id DESC LIMIT 1",
                               False))
        setattr(self, self.__class__.__name__.lower() + "_id",
                createdObj.__dict__[self.__class__.__name__.lower() + "_id"])

    def update(self) -> None:
        query = f"UPDATE {self.__class__.__name__.lower()} SET "
        idPassed = False
        idValue = []
        for key, value in self.__dict__.items():
            if idPassed:
                query += f"{key} = '{str(value)}' , "
            else:
                idValue = [key, value]
                idPassed = True
        commit(query[:-2] + f" WHERE {idValue[0]} = {idValue[1]}")

    def delete(self) -> int:
        query = f"DELETE FROM "+self.__class__.__name__.lower()+" WHERE "+self.__class__.__name__.lower()+"_id = "+str(self.__dict__[self.__class__.__name__.lower()+"_id"])
        return toObj(self.__class__.__name__, False, delete(query, False))
