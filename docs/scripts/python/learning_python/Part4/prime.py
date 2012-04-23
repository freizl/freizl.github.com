#!/cygdrive/c/Python25/python.exe

from __future__ import division

def prime1(y):
	if y <= 1:
		print y, 'not prime'
	else:
		x = y // 2
		while x > 1:
			if y % x == 0:
				retValue = y, 'has factor', x
				break
			x -= 1
		else:
			retValue = y, 'is prime'

def prime2(y):
	if y <= 1:
		print y, 'not prime'
	else:
		retValue = y, 'is prime'
		for x in range(y//2, 1, -1):
			if y % x == 0:
				retValue = y, 'has factor', x
				break
			

def timer(reps, func, *args):
	import time
	start = time.clock()
	for i in xrange(reps):
		map(func, args)
	return time.clock() - start

for func in (prime1,prime2):
	print timer(50000, func, 12,15,18,20,22,3000000)

