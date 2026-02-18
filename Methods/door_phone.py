class Door_Phone:
	def __init__(self):
		self.bell=False
		self.call=False
		self.is_camera_active=False
	def ring_bell(self):
		self.bell=True
		print("It will ring the bell")
	def make_call(self):
		self.call=True
		print("It will ring the phone")
	def camera_active(self):
		self.is_camera_active=True
		print("Camera gets Active")
		
	def status(self):
		print(f"Status: Bell={self.bell}, Call={self.call}, Camera Active={self.is_camera_active}")
        
door = Door_Phone()
door.ring_bell()
door.make_call()
door.camera_active()
door.status()