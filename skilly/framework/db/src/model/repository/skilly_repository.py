from skilly.framework.db.src.init.connect import commit, get
from skilly.framework.utils.src.skilly_utils import toObj


class Repository:

    @classmethod
    def joinQuery(cls, query):
        return get(query, True)
