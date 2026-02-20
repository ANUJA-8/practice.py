'''Create class Product:
name, price
method increase_price(percent)
Create class PriceManager:
static method that increases product price by given percent
prints updated price'''

class Product:
	def __init__(self,name:str,price:int):
		self.name=name
		self.price=price
	def increase_price(percent):
		return percent
		#self.price= self.price *percent/100
		
class PriceManager:
	def updated_price(p:Product,percent):
		updated_price = p.price + (p.price * percent / 100)
		print(f"Updated price of {p.name} is {updated_price}")
		
per=Product("Laptop", 50000)
PriceManager.updated_price(per,20)