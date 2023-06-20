
class Sql:

    def __init__(self, o):
        self.o = o

    @classmethod
    def string(cls, length):
        return Sql(f"VARCHAR({length}),")

    @classmethod
    def int(cls):
        return Sql("INT,")

    @classmethod
    def float(cls):
        return Sql("FLOAT,")

    @classmethod
    def datetime(cls):
        return Sql("DATETIME,")

    @classmethod
    def date(cls):
        return Sql("DATE,")

    @classmethod
    def time(cls):
        return Sql("TIME,")

    def id(self):
        return self.o[:-1] + " AUTO_INCREMENT PRIMARY KEY,"

    def notNull(self):
        return self.o[:-1] + " NOT NULL,"

