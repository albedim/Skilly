import datetime


class Entity:

    def toJSON(self, **kvargs):
        obj = {}
        for key in self.__dict__:
            if key != '__module__' \
                    and key != '__dict__' \
                    and key != '__weakref__' \
                    and key != '__doc__' \
                    and key != '__init__':
                obj[key] = self.__dict__[key] if type(self.__dict__[key]) == str or type(self.__dict__[key]) == int else str(self.__dict__[key])
        if len(kvargs) > 0:
            for kvarg in kvargs:
                obj[kvarg] = kvargs[kvarg]
        return obj

