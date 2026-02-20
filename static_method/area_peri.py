'''Create class Rectangle:
length, width
method area()
method perimeter()
Create class Geometry:
static method that prints both area and perimeter'''

class Rectangle:
	def __init__(self,length:int,width:int):
		self.length=length
		self.width=width
	def area(self):
		area=self.length*self.width
		return area
	def perimeter(self):
		perimeter= 2*(self.length+self.width)
		return perimeter
		
class Geometry:
	def area_peri(g:Rectangle):
		print(f"Area of the rectangle is {g.area()} and perimeter is {g.perimeter()}")
		
g1=Rectangle(5,4)
Geometry.area_peri(g1)