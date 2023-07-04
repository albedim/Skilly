from project.model.entity.myuser import MyUser
from project.model.repository.myuser_repository import MyUserRepository

#user = MyUser("albe", "dimaio")
#MyUserRepo.save(user)


class MyUserService:

    @classmethod
    def getAllUsers(cls):
        users: list[MyUser] = MyUserRepository.getOrderbyIdAsc()
        return users[0].toJSON()



