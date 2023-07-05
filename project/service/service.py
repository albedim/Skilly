import json

from project.model.entity.myuser import MyUser
from project.model.repository.myuser_repository import MyUserRepository
from skilly.framework.utils.src.controller.response_handler import ResponseHandler
from skilly.framework.utils.src.decorators.skilly_decorators import schema


#user = MyUser("albe", "dimaio")
#MyUserRepo.save(user)


class MyUserService:

    @classmethod
    def getAllUsers(cls):
        users: list[MyUser] = MyUserRepository.get()
        r = []
        for user in users:
            r.append(user.toJSON())
        return ResponseHandler(http=ResponseHandler.HTTP_CREATED, response=r).send()

    @classmethod
    def getUserById(cls, userId):
        user: MyUser = MyUserRepository.getByIdEq(userId)
        return ResponseHandler(
            http=ResponseHandler.HTTP_CREATED,
            response=user.toJSON()
        ).send()

    @classmethod
    def removeAll(cls):
        users: list[MyUser] = MyUserRepository.delete()
        r = []
        for user in users:
            r.append(user.toJSON())
        return ResponseHandler(
            http=ResponseHandler.HTTP_CREATED,
            response=r
        ).send()

    @classmethod
    @schema("CREATION")
    def add(cls, body):
        user = MyUser(body['name'], body['email'])
        MyUserRepository.save(user)
        return ResponseHandler(http=ResponseHandler.HTTP_CREATED, response={}).send()

    @classmethod
    def update(cls, userId, name):
        user: MyUser = MyUserRepository.getByIdEq(userId)
        user.name = name
        MyUserRepository.update(user)
        return ResponseHandler(http=ResponseHandler.HTTP_CREATED, response=user.toJSON()).send()




