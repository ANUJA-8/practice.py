'''Create class Circle:
radius
method area()
Create class ShapeFactory:
static method that creates a Circle object
prints its area'''

class Circle:
	def __init__(self,radius:int):
		self.radius=radius
		
	def area(self):
		return 3.14*self.radius*self.radius
		
class ShapeFactory:
	def area_circle(rad:Circle):
		# circle=Circle(radius)
		print(f"Area of circle with radius {rad.radius}cm is {rad.area()}cm^2")
		
r=Circle(4)
ShapeFactory.area_circle(r)