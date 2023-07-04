class Entity:

    def toJSON(self, **kvargs):
        if len(kvargs) == 0:
            return self.__dict__
        obj = self.__dict__
        for kvarg in kvargs:
            obj[kvarg] = kvargs[kvarg]
        return obj
