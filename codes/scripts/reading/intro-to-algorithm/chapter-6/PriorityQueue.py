#!/usr/bin/python

from heaps import *

class PriorityQueue(object):
    def __init__(self, A):
        self.A = A
        build_max_heap(self.A)

    def heap_maximum(self):
        return self.A[0]

    def heap_extract_max(self):
        # if heap_size < 1, raise error..
        i_last = heap_size(self.A) - 1
        swap(self.A, 0, i_last)
        max = self.A.pop(i_last)
        max_heapify(self.A, 1)
        return max

    # Can not leverage max_heapify as max_heapify is Top Down,
    # but heap_increase_key is Bottom Up
    def heap_increase_key(self, i, key):
        # if self.A[i] > key, raise error
        self.A[i-1] = key
        while i > 1 and self.A[parent(i)-1] < self.A[i-1]:
            swap(self.A, i-1, parent(i)-1 )
            i = parent(i)

    def heap_insert_key(self, key):
        self.A.append(-1)
        self.heap_increase_key(heap_size(self.A), key)

    def __str__(self):
        return self.A.__str__()

if __name__ == '__main__':
    queue = PriorityQueue([16,4,10,14,7,9,3,2,8,1])
    key = 15
    print "priority queue: %s" % queue
    print "highest priority item: %d" % queue.heap_maximum()

    print "increase priority of 9th item from %d to %d" % (queue.A[8], key)
    queue.heap_increase_key(9, key)
    print "the queue is re build to: %s" % queue

    key = queue.heap_extract_max()
    print "dequeue highest priority item: %d" % key
    print "the queue afterwards: %s" % queue

    print "add the removed item %d back" % key
    queue.heap_insert_key(key)
    print " %s " % queue
