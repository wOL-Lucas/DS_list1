class Buy:
    def __init__(self, product):
        self.product = product

    def calculate_total(self):
        if product.quantity >= 10:
            return product.price * product.quantity * 0.9

class Product:
    def __init__(self):
        self.name: str = None
        self.price: float = None
        self.quantity: int = None



product = Product()
product.name = input('Enter the product name: ')
product.price = float(input('Enter the product price: '))
product.quantity = int(input('Enter the product quantity: '))

buy = Buy(product)

print(f'Total: {buy.calculate_total()}')
