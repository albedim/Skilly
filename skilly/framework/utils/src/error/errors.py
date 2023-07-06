class NotFoundError(Exception):

    @classmethod
    def getMessage(cls):
        return "[skilly.error] -> This element was not found"


class UnmappableQueryResult(Exception):

    @classmethod
    def getMessage(cls):
        return "[skilly.error] -> This query result can't be mapped into a Skilly.entity class"


class InconvertibleEntityToJSON(Exception):

    @classmethod
    def getMessage(cls):
        return "[skilly.error] -> This entity object can't be converted into JSON"

