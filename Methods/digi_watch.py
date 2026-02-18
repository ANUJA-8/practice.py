class DigitalWatchAlaram:
	def __init__(self,current_time:float,wake_up_time:float):
		self.current_time=current_time
		self.wake_up_time=wake_up_time
		self.wake_snooz_time=0.0
		self.alaram_is_on=False
	def digital_alaram(self,status:str):
		if self.current_time==self.wake_up_time:
			self.alaram_is_on=True
			# print(f"Alaram is on and the current time is {self.current_time}")
			if status=="snooz":
				self.wake_snooz_time=self.wake_up_time+00.10
				self.alaram_is_on=True
				print(f"Alaram will ring in 10 minutes at {self.wake_snooz_time}")
			elif status=="off":
				self.alaram_is_on=False
				print("Alaram is off")
			elif status=="":
				self.wake_up_time=self.wake_up_time+00.05
				self.alaram_is_on=True
				print(f"Alaram will ring in 5 minutes at {self.wake_up_time}")
			
		self.alaram_is_on=False
		# print(f"Alaram is off and the current time is {self.current_time}")
     
digi_watch=DigitalWatchAlaram(3.15,3.15)
digi_watch.digital_alaram("")
			

		