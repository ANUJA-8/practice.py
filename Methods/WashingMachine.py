class WashingMachine:
	def __init__(self,Water_level:int,weight:int):
		self.water_level=Water_level
		self.weight=weight
		self.machine_is_on=False
	def wash(self):
		if 8>self.water_level>2 and self.weight<8:
			self.machine_is_on=True
			print("Washing machine has started")
		else:
			self.machine_is_on=False
			print("Either the water is not in tub or the cloths")

WM=WashingMachine(4,6)
WM.wash()