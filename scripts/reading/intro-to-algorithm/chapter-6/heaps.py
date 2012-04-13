#!/usr/bin/python
import time

def parent(i):
    return i/2

def left(i):
    return i * 2

def right(i):
    return i * 2 + 1

## TODO any build in function?
def swap(A, i, j):
    tmp = A[i]
    A[i] = A[j]
    A[j] = tmp

def heap_size(A):
    return len(A)

### i is index of heap tree but not index of the array
### thus minus i when operation on the array
def max_heapify(A, i, hsize=None):
    l = left(i)
    r = right(i)
    h_size = hsize or heap_size(A)
    if l <= h_size and A[l-1] > A[i-1]:
        largest = l
    else:
        largest = i
    if r <= h_size and A[r-1] > A[largest-1]:
        largest = r
    if largest != i:
        swap(A, largest-1, i-1)
        max_heapify(A, largest, hsize=h_size)

def build_max_heap(A):
    for i in range(len(A)/2, 0, -1):
        max_heapify(A, i)

"""
HEAPSORT(A)
1 BUILD-MAX-HEAP(A)
2 for i <- length[A] downto 2
3    do exchange A[1] <-> A[i]
4       heap-size[A] <- heap-size[A] - 1
5       MAX-HEAPIFY(A, 1)
"""
def heap_sort(A):
    start = time.time()

    build_max_heap(A)
    print "[heap_sort] time for building %d array: %f" % (len(A), time.time() - start)

    for i in range(heap_size(A), 1, -1):
        swap(A, i-1, 0)
        max_heapify(A, 1, i-1)
    print "[heap_sort] time for sorting array: %f" % (time.time() - start)

if __name__ == '__main__':
    test_array = [16,4,10,14,7,9,3,2,8,1]
    max_heapify(test_array, 2)
    print test_array

#    test_array = [4,1,3,2,16,9,10,14,8,7,4,1]
#    build_max_heap(test_array)
#    print test_array
#
    heap_sort(test_array)
    print test_array

