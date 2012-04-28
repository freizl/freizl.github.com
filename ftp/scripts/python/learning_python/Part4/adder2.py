#!/cygdrive/c/Python25/python.exe

def adder(good='good ', bad='bad ', ugly='ugly '):
	return good + bad + ugly

def adder1(*args):
	print 'adder1',
	print type(0),
	if type(args[0]) == type(0):
		sum = 0
	else:
		sum = args[0][:0]
	for arg in args:
		sum = sum + arg
	return sum

def adder2(*args):
	print 'adder2',
	sum = args[0]
	for next in args[1:]:
		sum = sum + next
	return sum

for func in (adder1, adder2):
	#print func()
	print func(2,3,4)
	print func('spam','eggs','toast')
	print func(['a','b','c'],['e','f'])
