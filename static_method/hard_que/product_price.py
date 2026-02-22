'''Create class Product:
name
price
Methods:
reduce_price(amount)
get_price()
Create class Market:
static method price_war(prod1, prod2)
Reduce price of the more expensive product by 10%
Print updated prices'''

class Product:
	def __init__(self,name:str,price:int):
		self.name=name
		self.price=price
	def reduce_price(self,amount):
		self.price-=amount
		return self.price
	def get_price(self):
		return self.price
		
class Market:
	def price_war(pr1:Product,pr2:Product):
		if pr1.price> pr2.price:
			reduce=pr1.price/10
			print(f"{pr1.reduce_price(reduce)} is the updated price of the {pr1.name}product" )
		elif pr1.price< pr2.price:
			reduce=pr2.price/10
			print(f"{pr2.reduce_price(reduce)} is the updated price of the {pr2.name} product" )
		else:
			print(f"{pr1.name} and {pr2.name}both have same price")
	# def updated_prices():
		print(f"Price of product {pr1.name} is {pr1.price}")
		print(f"Price of product {pr2.name} is {pr2.price}")
		
prod1=Product("Laptop", 50000)
prod2=Product("LED", 30000)

Market.price_war(prod1,prod2)
# Market.updated_prices()