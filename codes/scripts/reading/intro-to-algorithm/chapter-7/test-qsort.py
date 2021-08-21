#!/usr/bin/python

from qsort import *
import random
import time

"""
- around 15 seconds for 1 millison items
- (RuntimeError: maximum recursion depth exceeded) when sorting sorted array,e.g. n>1000
"""
if __name__ == '__main__':

    start = time.time()

    a = [random.randint(1,i) for i in range(1,1000)]

    middle = time.time()
    print "time for building %d array: %f" % (len(a), middle - start)
    b = a[:]

    qsort(a, 0, len(a)-1)
    time_qsort = time.time()
    print "time for qsort: %f" % (time_qsort - middle)

    random_qsort(b, 0, len(b)-1)
    print "time for random qsort: %f" % (time.time() - time_qsort)
