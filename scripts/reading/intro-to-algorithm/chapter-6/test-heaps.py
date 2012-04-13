#!/usr/bin/python

from heaps import *
import random
import time

"""
take 45 seconds to sort 1 millison numbers
"""
if __name__ == '__main__':

    start = time.time()

    a = [random.randint(1,i) for i in range(1,1000)]
    print "time for building %d array: %f" % (len(a), time.time() - start)

    heap_sort(a)
    print "time for build heap: %f" % (time.time() - start)
