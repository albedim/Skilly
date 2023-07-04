from project.model.entity.myuser import MyUser
from skilly.framework.utils.src.decorators.skilly_decorators import autoQBN
from skilly.framework.db.src.model.repository.skilly_repository import Repository


class MyUserRepository(Repository):

    @classmethod
    @autoQBN
    def getByNameEq(cls, name: str) -> MyUser: ...

    @classmethod
    @autoQBN
    def getOrderbyIdAsc(cls) -> list[MyUser]: ...

    @classmethod
    @autoQBN
    def deleteByNameEqLimit1(cls, name: str) -> MyUser: ...