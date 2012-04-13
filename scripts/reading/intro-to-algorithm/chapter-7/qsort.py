#!/usr/bin/python

import random

def swap(A, i, j):
    tmp = A[i]
    A[i] = A[j]
    A[j] = tmp

def qsort(A, p, r):
    if p < r:
        q = parition(A, p, r)
        qsort(A, p, q-1)
        qsort(A, q+1, r)

def parition(A, p, r):
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= x:
            i = i + 1
            swap(A, i, j)
    swap(A, i+1, r)
    return i+1

def random_parition(A, p, r):
    i = random.randint(p, r)
    swap(A, i, r)
    return parition(A, p, r)

# Test result shows random_sort performaces worse than qsort.
# It is not desirable. Any bug?
def random_qsort(A, p, r):
    if p < r:
        q = random_parition(A, p, r)
        random_qsort(A, p, q-1)
        random_qsort(A, q+1, r)

if __name__ == '__main__':
    a = [2,8,7,1,3,5,6,4]
    qsort(a,0,len(a)-1)
    print a

    b = [2,8,9,7,1,3,5,6,4]
    random_qsort(b,0,len(b)-1)
    print b
