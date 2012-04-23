
class FirstClass:
	def setdata(self, value):
		self.data = value
	def display(self):
		print "data value at FirstClass: %s " % self.data

class SecondClass(FirstClass):
	def display(self):
		print "data value at Second Class: %s" % self.data

class ThirdClass(SecondClass):
	def __init__(self, value):
		self.data = value
	def __add__(self, other):
		return ThirdClass(self.data + other)
	def __mul__(self, other):
		self.data = self.data * other

def first_class_test():
	print "="*8,"I am the first class tester ..."
	x = FirstClass()
	y = FirstClass()
	x.setdata("King Arthur")
	y.setdata(3.1415)
	FirstClass.data = "none"
	x.display()
	y.display()

def second_class_test():
	print "="*8, "I am the second class tester ..."
	x = FirstClass()
	x.setdata("default value")
	z = SecondClass()
	z.setdata(42)
	z.display()
	x.display()

def third_class_test():
	print "="*8, "I am the second class tester ..."
	a = ThirdClass("abc")
	a.display()
	b = a + "xyz"
	b.display()
	a * 3
	a.display()

if __name__ == "__main__":
	first_class_test()
	second_class_test()
	third_class_test()
