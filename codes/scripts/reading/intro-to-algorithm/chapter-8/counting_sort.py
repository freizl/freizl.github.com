#!/usr/bin/python

import random

"""
C[2] = 3, it means there are 3 items that less or equal then 2
"""
def counting_sort(A, key):
    C = [0] * (key+1)
    B = [0] * len(A)

    for i in A:
        C[i] = C[i] + 1
    for i in range(1, len(C)):
        C[i] = C[i] + C[i-1]

    for i in range(len(B)-1, -1, -1):
#    for i in range(0, len(B)):
        B[C[A[i]]-1] = A[i]
        C[A[i]] = C[A[i]] - 1
    return B

if __name__ == '__main__':
    a = [2,5,3,0,2,3,0,3]
    key = max(a)
    print counting_sort(a, key)

