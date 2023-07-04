from project.model.entity.myuser import MyUser
from project.service.service import MyUserService
from skilly.framework.db.src.init.skilly_init import entityInit

routes = entityInit(MyUser)

print(MyUserService.getAllUsers())
