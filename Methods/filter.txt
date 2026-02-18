class filter:
	def __init__(self,capacity:int):
		self.capacity=capacity
		self.current_level=0
		self.filter_ison= False
	def water_filter(self):
		self.filter_ison=True
		print(f"Water filtering is started")
		
		while self.filter_ison:
			self.fill_water(1)
	def filter_water(self,amount:int):
		if self.current_level+amount>=self.capacity:
			self.current_level=self.capacity
			print(f"{self.current_level} lit.")
			
			self.auto_off()
		else:
			self.current_level+=amount
			print(f"filling water current level is {self.current_level}lit ")
	def auto_off(self):
		self.filter_ison=False
		print("Filter is fulled")

filter1=filter(4)
filter1.filter_water(4)
