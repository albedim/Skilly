import inspect

from skilly.framework.db.src.init.skilly_connect import commit, get, delete
from skilly.framework.db.src.model.entity.skilly_entity import Entity
from skilly.framework.db.src.model.entity.skilly_generic_entity import GenericEntity
from skilly.framework.utils.src.error.errors import InvalidParamsAmount
from skilly.framework.utils.src.skilly_utils import toObj, Attr


class Repository:

    entities = list()

    def __init__(self, entities, query):
        self.query = query
        if len(entities) == 2:
            self.entities.clear()
        for entity in entities:
            self.entities.append(entity)

    @classmethod
    def startJoin(cls, leftEntity, rightEntity):
        query = "SELECT * from " + leftEntity.__name__ + " join " + rightEntity.__name__
        return Repository(
            [leftEntity, rightEntity],
            "SELECT * from " + leftEntity.__name__ + " join " + rightEntity.__name__)

    @classmethod
    def manualQBN(cls, fetchAll: bool, query: str, *keys: Attr):
        if fetchAll:
            res = get(query, fetchAll)

            if len(res[0]) != len(keys):
                raise InvalidParamsAmount(InvalidParamsAmount.getMessage())

            mylist = []
            for r in res:
                counter = 0
                obj = GenericEntity()
                for key in keys:
                    setattr(obj, key.attribute, r[counter])
                    counter += 1
                mylist.append(obj)
            return mylist
        else:
            res = get(query, fetchAll)
            counter = 0

            if len(res) != len(keys):
                raise InvalidParamsAmount(InvalidParamsAmount.getMessage())

            baseObj = GenericEntity()
            for key in keys:
                setattr(baseObj, key.attribute, res[counter])
                counter += 1
            return baseObj

    def join(self, entity):
        query = " join " + entity.__name__
        return Repository([entity], self.query + query)

    def on(self, leftVar, rightVar):
        return Repository([], self.query + " ON " + leftVar + " = " + rightVar)

    def where(self, key, operand, value):
        if type(value) == int:
            value = str(value)
        else:
            value = "'" + value + "'"
        return Repository([], self.query + " WHERE " + key + " " + operand + " " + value)

    def _and(self, key, operand, value):
        return Repository([], self.query + " AND " + key + " " + operand + " " + value)

    def _or(self, key, operand, value):
        return Repository([], self.query + " OR " + key + " " + operand + " " + value)

    def execute(self, split=True):
        print(self.entities, self.query)
        if split:
            query = get(self.query, True)
            result = []
            for i in range(len(query)):
                res = []
                counter = 0
                for entity in self.entities:
                    length = len(entity.__dict__) - 3 + counter
                    newTuple = ()
                    while counter < length:
                        newTuple += query[i][counter],
                        counter += 1
                    print(newTuple)
                    res.append(toObj(entity.__name__, False, newTuple))
                result.append(res)
            print(result)
            return result
            pass
        else:
            query = get(self.query, True)
            result = []
            for i in range(len(query)):
                res = {}
                counter = 0
                for entity in self.entities:
                    for e in entity.__dict__:
                        if e != '__module__' and e != '__dict__' and e != '__weakref__' and e != '__doc__' and e != '__init__':
                            res[entity.__name__.lower() + "." + e] = query[i][counter]
                            counter += 1
                result.append(res)
            print(result)
            return result