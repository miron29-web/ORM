class Field:
    def __init__(self,
                 name=None,
                 null=False, 
                 unique=False, 
                 primary_key=False
                 ):
        
        self.__name = name
        self.__null = null
        self.__unique = unique
        self.__primary_key = primary_key

class CharField(Field):
    def __init__(self, 
                 max_length=None,
                 **kwargs
                 ):
        
        self.field_type = 'TEXT'
        self.__max_length = max_length

        super().__init__(**kwargs)

class IntegerField(Field):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)