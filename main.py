from orm.fields import CharField, IntegerField
from orm.models.model import Model

class Product(Model):
    id = IntegerField()
    title = CharField(max_length=100)


def main():
    product = Product()
    product.title = "хлеб"
    product.create_table()

if __name__ == '__main__':
    main()