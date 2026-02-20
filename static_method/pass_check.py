'''Create class User:
username, password
method check_password_length()
Create class Validator:
static method that prints if password is valid (length ≥ 8)'''
		
class User:
	def __init__(self,username:str,password): #here we can pass self only if we want to initiate an variable in the class and if we want to use that variable in other method then we have to use self to access that variable ex. self.count=0
		self.username=username
		self.password=password
	def check_password_length(self):
		length=len(self.password)  #self.password is used to acess the password variable used in above method "self" is needed
		return length
class Validator:
	def valid_len(l:User):
		if l.check_password_length()>=8:   #use method of previous class instead of using the variable(length) directly
			return f"{l.password} is valid"  #you can use return here but if you return here you have to print the function call and if you use print here then you can directly call the function without print
		else:
			return f"{l.password} is not valid"
		# if l.check_password_length()>=8:
        # 	print(f"{l.password} is valid")
		# else:
		# 	print(f"{l.password} is not valid")
		
p=User("Akash","Akash@123")
print(Validator.valid_len(p))
# Validator.valid_len(p) #if you use print in the function then you can directly call the function without print and if you use return then you have to print the function call to see the output