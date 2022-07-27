# Python program to demonstrate private members Creating a Base class

class Base:
	def __init__(self):
		self.a = "hello"
		self.__b = "Sarbjeet"

# Creating a derived class
class Derived(Base):
	def __init__(self):

		# Calling constructor of Base class
		Base.__init__(self)
		print("Calling private member of base class: ")
		print(self.__b)


# Driver code
obj1 = Base()
print(obj1.a)

# Uncommenting print(obj1.__c) will
# raise an AttributeError

# Uncommenting obj2 = Derived() will
# also raise an AtrributeError as
# private member of base class
# is called inside derived class
