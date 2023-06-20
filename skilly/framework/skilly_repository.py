
class Repository:

    @classmethod
    def save(cls, o):
        query = "INSERT INTO {table} VALUES(NULL, "
        for prop in o.__dict__:
            query += f"'{str(o.__dict__[prop])}' , "
        print(query[:-2] + ")")
        return o

    @classmethod
    def update(cls, o):
        query = "UPDATE {table} SET "
        idPassed = False
        idValue = []
        for key, value in o.__dict__.items():
            if idPassed:
                query += f"{key} = '{str(value)}' , "
            else:
                idValue = [key, value]
                idPassed = True
        print(query[:-2] + f" WHERE {idValue[0]} = {idValue[1]}")
        return o


def createQuery(f, *params):
    try:
        newF = f.__name__ + "A"
        i = 0
        counter = 0
        j = 0
        finalQuery = ""
        while i <= len(newF):
            done = False
            while not done:
                if newF[j].isupper() or newF[j].isnumeric():
                    thisF = newF[i:j].lower()
                    i = j
                    for key in DICTIONARY:
                        if key == thisF:
                            finalQuery += DICTIONARY[key]["value"]
                            if DICTIONARY[key]["operand"]:
                                finalQuery += str(params[counter])
                                counter += 1
                            if DICTIONARY[key]["inline-operand"]:
                                finalQuery += newF[j - 1]
                            break
                        elif key == "last":
                            finalQuery += thisF
                    done = True
                j += 1
        return finalQuery
    except IndexError:
        return finalQuery


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
