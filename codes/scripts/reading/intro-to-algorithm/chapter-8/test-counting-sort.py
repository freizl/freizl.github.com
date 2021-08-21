#!/usr/bin/python

from counting_sort import counting_sort
import random
import time

if __name__ == '__main__':
    start = time.time()

    a = [random.randint(0,i) for i in range(10,100000)]

    middle = time.time()
    print "time for building %d array: %f" % (len(a), middle - start)

    counting_sort(a, max(a))
    time_qsort = time.time()
    print "time for qsort: %f" % (time_qsort - middle)

