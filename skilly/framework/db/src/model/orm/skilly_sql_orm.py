from skilly.framework.db.src.init.skilly_connect import get, delete
from skilly.framework.utils.src.skilly_utils import toObj


class Sql:
    """
    # Returns an object of Sql
        # Parameters:
            o (Sql): object of Sql with basic query inside
        # Returns:
            object (Sql): Sql object
    """

    def __init__(self, o):
        self.o = o

    """
    # Returns an object of Sql with o = varchar...
        # Parameters:
            length (int): length of the varchar
        # Returns:
            object (Sql): Sql object
    """

    @classmethod
    def string(cls, length):
        return Sql(f"VARCHAR({length}),")

    """
    # Returns an object of Sql with o = int...
        # Parameters:
            -
        # Returns:
            object (Sql): Sql object
    """

    @classmethod
    def int(cls):
        return Sql("INT,")

    """
    # Returns an object of Sql with o = float...
        # Parameters:
            -
        # Returns:
            object (Sql): Sql object
    """

    @classmethod
    def float(cls):
        return Sql("FLOAT,")

    """
    # Returns an object of Sql with o = datetime...
        # Parameters:
            -
        # Returns:
            object (Sql): Sql object
    """

    @classmethod
    def datetime(cls):
        return Sql("DATETIME,")

    """
    # Returns an object of Sql with o = date...
        # Parameters:
            -
        # Returns:
            object (Sql): Sql object
    """

    @classmethod
    def date(cls):
        return Sql("DATE,")

    """
    # Returns an object of Sql with o = time...
        # Parameters:
            -
        # Returns:
            object (Sql): Sql object
    """

    @classmethod
    def time(cls):
        return Sql("TIME,")

    """
    # Returns an object of Sql with o += auto_increment primary key...
        # Parameters:
            -
        # Returns:
            query (str): final query
    """

    def id(self, primary_key=False):
        if primary_key:
            return self.o[:-1] + " AUTO_INCREMENT PRIMARY KEY,"
        return self.o[:-1] + ","

    """
    # Returns an object of Sql with o += not null...
        # Parameters:
            -
        # Returns:
            query (str): final query
    """

    def notNull(self):
        return self.o[:-1] + " NOT NULL,"

    def allowNull(self):
        return self.o


"""
# Returns an object which is going to be returned by a function that 
# converts a tuple to an object of a specific class given in the params
    # Parameters:
        f (func): function
        *params (tuple): function params
    # Returns:
        object (any): Entity object
"""


def createQuery(f, *params) -> None:
    try:
        # newF will be the name of the function
        newF = f.__name__ + "A"
        # begin index of word
        i = 0
        counter = 0
        # last index of word
        j = 0
        finalQuery = ""
        # boolean var to check if the return type of the function is list, so it is going to return a list of objects
        isList = f.__annotations__["return"].__name__.lower() == "list"
        isDelete = newF.startswith("delete")
        entityName = str(f.__annotations__["return"]).split(".")[-1][:-1] if isList else f.__annotations__[
            "return"].__name__
        while i <= len(newF):
            # variable to check if a word is done
            done = False
            # if the word is not done, i will be at the begin of the new word,
            # j will go next until it finds the nex upper case or number
            while not done:
                if newF[j].isupper() or newF[j].isnumeric():
                    # thisF will be the function name[i:j] getByName -> get
                    thisF = newF[i:j].lower()
                    # i will be set to j so that the next word will be starting at the end of the old one
                    i = j
                    for key in DICTIONARY:
                        # if it finds this word in the dictionary, it will be replaced with sql
                        if key == thisF:
                            finalQuery += DICTIONARY[key]["value"].replace("{table}", entityName)
                            # if it's an operand, it means that there will be a value after it
                            # so it will be added one of the params
                            if DICTIONARY[key]["operand"]:
                                finalQuery += str(params[counter]) if str(
                                    params[counter]).isnumeric() else f"'{str(params[counter])}'"
                                counter += 1
                            if DICTIONARY[key]["inline-operand"]:
                                finalQuery += newF[j]
                                newF = newF[:-2]
                            break
                        elif key == "last":
                            finalQuery += thisF
                    done = True
                j += 1
        if isDelete:
            return toObj(entityName, isList, delete(finalQuery, fetchAll=isList))
        return toObj(entityName, isList, get(finalQuery, fetchAll=isList))
    except IndexError:
        if isDelete:
            return toObj(entityName, isList, delete(finalQuery, fetchAll=isList))
        return toObj(entityName, isList, get(finalQuery, fetchAll=isList))


DICTIONARY = {
    "get": {
        "value": "SELECT * FROM {table}",
        "operand": False,
        "inline-operand": False
    },
    "delete": {
        "value": "DELETE FROM {table}",
        "operand": False,
        "inline-operand": False
    },
    "and": {
        "value": " AND ",
        "operand": False,
        "inline-operand": False
    },
    "or": {
        "value": " OR ",
        "operand": False,
        "inline-operand": False
    },
    "by": {
        "value": " WHERE ",
        "operand": False,
        "inline-operand": False
    },
    "eq": {
        "value": " = ",
        "operand": True,
        "inline-operand": False
    },
    "gt": {
        "value": " > ",
        "operand": True,
        "inline-operand": False
    },
    "gte": {
        "value": " >= ",
        "operand": True,
        "inline-operand": False
    },
    "lt": {
        "value": " < ",
        "operand": True,
        "inline-operand": False
    },
    "lte": {
        "value": " <= ",
        "operand": True,
        "inline-operand": False
    },
    "orderby": {
        "value": " ORDER BY ",
        "operand": False,
        "inline-operand": False
    },
    "asc": {
        "value": " ASC ",
        "operand": False,
        "inline-operand": False
    },
    "desc": {
        "value": " DESC ",
        "operand": False,
        "inline-operand": False
    },
    "limit": {
        "value": " LIMIT ",
        "operand": False,
        "inline-operand": True
    },
    "last": {
        "value": "",
        "operand": False,
        "inline-operand": False
    },
}
