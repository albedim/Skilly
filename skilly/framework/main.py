from skilly.framework.skilly_decorators import entity, autoQBN
from skilly.framework.skilly_init import entityInit
from skilly.framework.skilly_repository import Repository
from skilly.framework.skilly_sql_orm import Sql
from skilly.framework.skilly_init import entityInit


class MyUser:

    id = Sql.int().id()
    name = Sql.string(40).notNull()
    email = Sql.string(40).notNull()

    @entity
    def __init__(self, name, email, obj=()): ...


app = entityInit(MyUser)


class MyUserRepo(Repository):

    @classmethod
    @autoQBN
    def getByNameEq(cls, name: str) -> MyUser: ...

    @classmethod
    @autoQBN
    def getOrderbyIdAsc(cls) -> list[MyUser]: ...

    @classmethod
    @autoQBN
    def deleteByNameEqLimit1(cls, name: str) -> MyUser: ...

#user = MyUser("albe", "dimaio")
#MyUserRepo.save(user)

users: list[MyUser] = MyUserRepo.getOrderbyIdAsc()
print(users[0].id)







