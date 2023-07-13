import datetime

from skilly.framework.db.src.init.skilly_connect import commit, get, delete
from skilly.framework.db.src.model.entity.skilly_entity import Entity
from skilly.framework.utils.src.error.errors import UnmappableQueryResult, InconvertibleEntityToJSON
from skilly.framework.utils.src.skilly_utils import toObj


class GenericEntity(Entity):

    ...
