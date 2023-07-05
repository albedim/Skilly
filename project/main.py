from project.controller.myuser_controller import home
from project.model.entity.myuser import MyUser
from skilly.framework.db.src.init.skilly_init import entityInit

from project.controller.myuser_controller import *
from skilly.framework.server.src.server import run_server

entityInit(MyUser)

run_server()
