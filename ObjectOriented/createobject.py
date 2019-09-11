# A Sample class with init method
class Person:

	# init method or constructor
	def __init__(self, name):
		self.name = name
		print("this is been printed while creating an object")

	# Sample Method
	def say_hi(self):
		print('Hello, my name is', self.name)

p = Person('Shwetanshu')
p.say_hi()
