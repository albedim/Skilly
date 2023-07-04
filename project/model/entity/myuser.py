from skilly.framework.db.src.model.entity.skilly_entity import Entity
from skilly.framework.utils.src.decorators.skilly_decorators import entity
from skilly.framework.db.src.model.orm.skilly_sql_orm import Sql


class MyUser(Entity):
    id = Sql.int().id()
    name = Sql.string(40).notNull()
    email = Sql.string(40).notNull()

    @entity
    def __init__(self, name, email, obj=()): ...
