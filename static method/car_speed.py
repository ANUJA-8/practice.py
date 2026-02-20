'''Create class Car:
brand, speed
method is_speeding() (True if speed > 80)
Create class TrafficPolice:
static method that returns fine message if speeding'''
class Car:
	def __init__(self,brand:str,speed:int):
		self.brand=brand
		self.speed=speed
	def is_speeding(self):
		return self.speed> 80
		
class TrafficPolice:
	def fine(f:Car):
		# if f.is_speeding():
		# 	print(f"Apply fine for {f.brand}")
		# else:
		# 	print(f"No fine for {f.brand}")
		if f.is_speeding():
			return f"Apply fine for {f.brand}"
		return f"No fine for {f.brand}"
			
		
fi=Car("Honda",90)
# TrafficPolice.fine(fi)
print(TrafficPolice.fine(fi))
		