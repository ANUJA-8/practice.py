'''Product & BillCalculator
Create Product class with: name, price
with methods 
total(product1, product2)
apply_discount(product, percent)
Create BillCalculator class to call above methods:
'''
class Product:
	def __init__(self,name:str, price:int):
		self.name=name
		self.price=price
class Bill_product:
    def total(self,product1:Product, product2:Product):
        return f"Total price: {product1.price+product2.price}"
    def apply_discount(self,product:Product, percent:int):
        return f"Discounted price: {product.price-(product.price*percent/100)}"
pr1=Product("Laptop", 50000)
pr2=Product("Mouse", 1000)
bill_calculator=Bill_product()
print(bill_calculator.total(pr1, pr2))
print(bill_calculator.apply_discount(pr1, 10))

	