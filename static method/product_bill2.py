'''Product & BillCalculator
Create Product class with: name, price
with methods 
total(product1, product2)
apply_discount(product, percent)
Create BillCalculator class to call above methods:
'''
class Product:
    def __init__(self, name: str, price: int):
        self.name = name
        self.price = price


class BillCalculator:
    def total(product1: "Product", product2: "Product"):
        return product1.price + product2.price

    def apply_discount(product: "Product", percent: int):
        return product.price - (product.price * percent / 100)


# Testing
pr1 = Product("Laptop", 50000)
pr2 = Product("Mouse", 1000)

print("Total price:", BillCalculator.total(pr1, pr2))
print("Discounted price:", BillCalculator.apply_discount(pr1, 10))
