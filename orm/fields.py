class Field:
    def __init__(self, null=False, unique=False, primary_key=False):
        self.__null = null
        self.__unique = unique
        self.__primary_key = False

class CharField(Field):
    def __init__(self, max_lenght=None, **kwargs):
        self.__max_lenght = max_lenght
        super().__init__(**kwargs)

class IntegerField(Field):
    pass