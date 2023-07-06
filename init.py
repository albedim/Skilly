import datetime


def create_entity(entity_name):
    file = open("./model/entity/"+entity_name.lower()+"_entity.py", "w")
    file.write("""from skilly.framework.db.src.model.entity.skilly_entity import Entity
from skilly.framework.utils.src.decorators.skilly_decorators import entity
from skilly.framework.db.src.model.orm.skilly_sql_orm import Sql


class """+entity_name.lower().capitalize()+"""(Entity):
    """+entity_name.lower()+"""_id = Sql.int().id()

    @entity
    def __init__(self, obj=()): ...
""")
    print(f"Entity '{entity_name}' created")


def create_repository(entity_name):
    file = open("./model/repository/"+entity_name.lower()+"_repository.py", "w")
    file.write("""from src.model.entity."""+entity_name.lower()+"""_entity import """+entity_name.lower().capitalize()+"""
from skilly.framework.utils.src.decorators.skilly_decorators import autoQBN
from skilly.framework.db.src.model.repository.skilly_repository import Repository


class """+entity_name.lower().capitalize()+"""Repository(Repository):

    @classmethod
    @autoQBN
    # this method gets a """+entity_name.lower()+""" by its userId
    def getBy"""+entity_name.lower().capitalize()+"""_idEq(cls, userId: int) -> """+entity_name.capitalize()+""": ...

""")
    file.close()
    print(f"Repository '{entity_name}' created")


def create_service(entity_name):
    file = open("./service/"+entity_name.lower()+"_service.py", "w")
    file.write("""import json
from src.model.entity."""+entity_name.lower()+"""_entity import """+entity_name.lower().capitalize()+"""
from src.model.repository."""+entity_name.lower()+"""_repository import """+entity_name.capitalize()+"""Repository
from skilly.framework.utils.src.controller.response_handler import ResponseHandler
from skilly.framework.utils.src.decorators.skilly_decorators import schema


class """+entity_name.lower().capitalize()+"""Service:

    @classmethod
    def get"""+entity_name.lower().capitalize()+"""(cls, """+entity_name.lower()+"""Id):
        """+entity_name.lower()+""": """+entity_name.lower().capitalize()+""" = """+entity_name.lower().capitalize()+"""Repository.getBy"""+entity_name.lower().capitalize()+"""_idEq("""+entity_name.lower()+"""Id)
        if """+entity_name.lower()+""" is None:
            return ResponseHandler(
                http=ResponseHandler.HTTP_NOT_FOUND,
                response={}
            ).setMessage("Not Found").send()
        else:
            return ResponseHandler(
                http=ResponseHandler.HTTP_CREATED,
                response="""+entity_name.lower()+""".toJSON()
            ).setMessage("Found").send()
        
    # ... you continue!

""")
    file.close()
    print(f"Service '{entity_name}' created")


def create_controller(entity_name):
    file = open("./controller/"+entity_name.lower()+"_controller.py", 'w')
    file.write("""from skilly.framework.utils.src.controller.router_handler import RouteHandler
from src.service."""+entity_name.lower()+"""_service import """+entity_name.lower().capitalize()+"""Service
from skilly.framework.server.src.decorators import route

router = RouteHandler('"""+entity_name.lower()+"""')

@route(router.new("/get/{"""+entity_name.lower()+"""_id}"), "GET")
def get"""+entity_name.lower().capitalize()+"""(request):
    """+entity_name.lower()+"""Id = request.variables('"""+entity_name.lower()+"""_id')
    result = """+entity_name.lower().capitalize()+"""Service.get"""+entity_name.lower().capitalize()+"""("""+entity_name.lower()+"""Id)
    return result

""")
    print(f"Controller '{entity_name}' created")


def main():
    print("Command Menu:")
    print(" - Create an entity create-entity <entityName>")
    print(" - Create a repository create-repository <entityName>")
    print(" - Create a service create-service <entityName>")
    print(" - Create a controller create-project <entityName>")
    print(" - Exit")

    while True:

        command = input("["+datetime.datetime.timestamp(datetime.datetime.now()).__str__().split(".")[0]+"]")

        if command.split(" ")[0] == "create-entity":
            create_entity(command.split(" ")[1])
        elif command.split(" ")[0] == "create-repository":
            create_repository(command.split(" ")[1])
        elif command.split(" ")[0] == "create-service":
            create_service(command.split(" ")[1])
        elif command.split(" ")[0] == "create-controller":
            create_controller(command.split(" ")[1])
        else:
            print("Invalid command. Please try again.")


if __name__ == "__main__":
    main()