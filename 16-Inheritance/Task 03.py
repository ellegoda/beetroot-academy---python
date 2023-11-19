class Product:
    def __init__(self, type, name, price):
        self.type = type
        self.name = name
        self.price = price


class ProductStore:
    def __init__(self):
        self.products = []
        self.income = 0

    def add_product(self, product, qty):
        self.products.append({'product': product, 'qty': qty})

    def add(self, product, qty):
        for item in self.products:
            if item['product'].name == product.name:
                item['qty'] += qty
                return
        self.add_product(product, qty)

    def set_discount(self, identifier, percent, identifier_type='name'):
        if identifier_type == 'name':
            for item in self.products:
                if item['product'].name == identifier:
                    item['product'].price *= (1 - percent / 100)
        elif identifier_type == 'type':
            for item in self.products:
                if item['product'].type == identifier:
                    item['product'].price *= (1 - percent / 100)
        else:
            raise ValueError("Invalid identifier_type. Use 'name' or 'type'.")

    def sell_product(self, product_name, qty):
        for item in self.products:
            if item['product'].name == product_name:
                if item['qty'] >= qty:
                    item['qty'] -= qty
                    self.income += qty * item['product'].price
                    return
                else:
                    raise ValueError("Not enough stock to sell.")

    def get_income(self):
        return self.income

    def get_all_products(self):
        return [(item['product'].type, item['product'].name, item['qty']) for item in self.products]

    def get_product_info(self, product_name):
        for item in self.products:
            if item['product'].name == product_name:
                return item['product'].type, item['product'].name, item['qty']
        raise ValueError("Product not found in the store.")


product1 = Product('Sport', 'Football T-Shirt', 100)
product2 = Product('Food', 'Ramen', 1.5)

store = ProductStore()

store.add(product1, 10)
store.add(product2, 300)

store.set_discount('Sport', 1)
store.set_discount('Food', 2, 'type')

store.sell_product('Football T-Shirt', 3)
store.sell_product('Ramen', 10)

print("Income:", store.get_income())
print("All products:", store.get_all_products())
print("Product info:", store.get_product_info('Football T-Shirt'))