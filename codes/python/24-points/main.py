#!/usr/bin/python

"""
 desc: ....
 TODO: whether to use parameter of op_perm and number_perm,
       size of n_tuple and o_tuple is diff with 1
"""

from __future__ import division
import os

# cant use: y == 0 and 0 or x / y
# because 0 eval to false, thus when y==0, it still performs x/y
def div (x,y):
    if y==0: return 0
    return x / y

# could leverage python built in module parse?
operation = {'+' : lambda x,y : x + y,
             '-' : lambda x,y : x - y,
             '*' : lambda x,y : x * y,
             '/' : lambda x,y : div(x,y)}

all_ops = operation.keys()

all_number_cand = (1,2,3,4,5,6,7,8,9,10)

def op_perm (ops=all_ops):
    return [(i,j,k) for i in ops for j in ops for k in ops]

def number_perm (numbers=all_number_cand):
    return [(i,j,k,l) for i in numbers for j in numbers for k in numbers for l in numbers]

### TODO proof this algorithm is correct or not
### TODO increase the performace, it takes 10s
def main ():
    result = []

    for n_tuple in number_perm():
        for o_tuple in op_perm():
            o_stack = list(o_tuple)
            n_stack = list(n_tuple)
            n_queue = list(n_tuple)
            while o_stack:
                op = operation[o_stack.pop()]
                n_stack.append(op(n_stack.pop(), n_stack.pop()))
                n_queue.insert(0, op(n_queue.pop(), n_queue.pop()))
            if 24 in n_stack or 24 in n_queue:
                result.append((' ').join([str(n_tuple),str(o_tuple),str(n_stack),str(n_queue)]))

    file = open('cal_res.txt','a')
    for item in result:
        file.writelines(item + os.linesep)
    file.close()

if __name__=='__main__':
    open('cal_res.txt','wb').write('') # any quick method?
    main()
