from project.product import Product


class ProductRepository:

    def __init__(self):
        self.products = []

    def add(self, product: Product):
        self.products.append(product)

    def find(self, product_name: str):
        for product in self.products:
            if product.name == product_name:
                return product
        return None

    def remove(self, product_name: str):
        to_delete = self.find(product_name)
        if to_delete is not None:
            self.products.remove(to_delete)

    def __repr__(self):
        result = ""
        count = 0
        for product in self.products:
            if count == 0:
                result += f"{product.name}: {product.quantity}"
            else:
                result += f"\n{product.name}: {product.quantity}"
            count += 1
        return result
