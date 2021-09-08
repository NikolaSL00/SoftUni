# Create a class Catalogue. The __init__ method should accept the name of the catalogue.
# Each catalogue should also have an attribute called products and it should be an empty list.

# The class should also have three more methods:
# add_product(product_name) - add the product to the products' list
# get_by_letter(first_letter) - returns a list containing only the products that start with the given letter
# __repr__ - returns the catalogue info in the following format:
# "Items in the {name} catalogue:
# {item1}
# {item2}
# …
# {itemN}"

# The items should be sorted alphabetically in ascending order.

class Catalogue:
    def __init__(self, name):
        self.name = name
        self.products = []

    def add_product(self, product_name):
        self.products.append(product_name)

    def get_by_letter(self, first_letter):
        goal_list = []
        for prod in self.products:
            if prod[0] == first_letter:
                goal_list.append(prod)
        return goal_list

    def __repr__(self):
        string = f"Items in the {self.name} catalogue:"
        self.products.sort()
        for el in self.products:
            string += f"\n{el}"
        return string


catalogue = Catalogue("Furniture")
catalogue.add_product("Sofa")
catalogue.add_product("Mirror")
catalogue.add_product("Desk")
catalogue.add_product("Chair")
catalogue.add_product("Carpet")
print(catalogue.get_by_letter("C"))
print(catalogue)

# EXPECTED OUTPUT:
# ['Chair', 'Carpet']
# Items in the Furniture catalogue:
# Carpet
# Chair
# Desk
# Mirror
# Sofa
