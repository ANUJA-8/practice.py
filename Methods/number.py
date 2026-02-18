class Number:
	def __init__(self,num):
		self.num=num
	def addition(self, other:"Number"):
		print(f"Addition of {self.num} and {other.num} is {self.num+other.num}")
	def multiplication(self, other:"Number"):
		print(f"Multiplication of {self.num} and {other.num} is {self.num*other.num}")
	def sub(self, other:"Number"):
		print(f"Subtraction of {self.num} and {other.num} is {self.num-other.num}")
	def __eq__(self, other:"Number"):
		return self.num==other.num
	def __gt__(self, other:"Number"):
		return self.num>other.num
	def __hash__(self):	
		return hash(self.num)
	def __str__(self):
		return f"{self.num}"
n1=Number(4)
n2=Number(5)
print(n1)
print(n1==n2)
print(n1>n2)
dict={}
dict[n1]=n1.num
dict[n1]=n1.num
print(dict)