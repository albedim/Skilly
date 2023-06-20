from skilly.framework.skilly_decorators import Entity, autoQBN, manualQBN
from skilly.framework.skilly_repository import Repository
from skilly.framework.skilly_sql_orm import Sql


class Ent:

    id = Sql.int().id()
    name = Sql.string(40).notNull()
    surname = Sql.string(40).notNull()
    age = Sql.int().notNull()

    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age


class Rep(Repository):

    @classmethod
    @autoQBN
    def getByNameEqAndAgeLt(cls, name: str, age: int): ...

e = Ent("a", "aa", 14)
Rep.save(e)
e.name = "afsfgasdgg"
e.id = 3
Rep.update(e)
print(Rep.getByNameEqAndAgeLt("alberto", 14))

"""

class MethodCrud:

    @classmethod
    def getByName(cls):
        return createQuery(cls.getByName, "alberto", "dimaio")

    @classmethod
    def getByIdEqAndAgeGte(cls):
        return createQuery(cls.getByIdEqAndAgeGte, "4", "18")


"""
