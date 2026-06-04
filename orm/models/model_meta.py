from ..fields import Field

class ModelMeta(type):
    def __new__(cls, name, bases, attrs):
    
        if name == "Model":
            return super().__new__(cls, name, bases, attrs)

        fields = dict()

        for key, value in attrs.items():
            if isinstance(value, Field):
                fields[key] = value

        attrs['_fields'] = fields

        return super().__new__(cls, name, bases, attrs)