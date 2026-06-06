from orm.fields import CharField, IntegerField, FloatField
from orm.models.model import Model

class Product(Model):
    table_name = "products"

    id = IntegerField(name="id", primary_key=True, autoincrement=True)
    title = CharField(max_length=100)
    price = FloatField()

def main():
    product1 = Product(title="Хлеб", price=100.00)
    product2 = Product(title="Масло", price=300.00)

    product1.create_table()
    product1.save()

if __name__ == '__main__':
    main()