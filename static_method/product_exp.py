'''Create class Product with:
name, price
method is_expensive() → True if price > 5000
Create class Store with static method to print whether product is expensive.'''

class Product:
	def __init__(self,name:str,price:int):
		self.name=name
		self.price=price
		
	def is_expensive(self):
		return self.price>=5000	
class Store:
	def check_pr_isexp(product_obj:Product):
		if product_obj.is_expensive():
			print(f"{product_obj.name} is expensive.")
		else:
			print(f"{product_obj.name} is not expensive.")
	
pr=Product("Laptop", 50000)
Store.check_pr_isexp(pr)