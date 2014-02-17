#!/usr/bin/python

""" Chapter 4, Python shortcuts """

def copy_test():
    org_list = [1, 2, 3, 4]
    same_list = org_list
    
    # org_list and same_list refer to the object
    same_list.append(6)
    print org_list, same_list
    
    # create a new copy of org_list
    copy_list = list(org_list) # same thing for dict/set
    copy_list.append(8)
    print copy_list, org_list


### get L[i] if i is valid otherwise return v
def list_get(L, i, v=None):
    if -len(L) <= i < len(L): return L[i]
    else: return v

### looping over items and their indexs
def looping_test():
    l = ["aaa", "bbb", "ccc"]
    for index, item in enumerate(l):
        print "Index:", index, "Content:", item

### multiple dimension array(list)
def lists_of_lists():
    # cannot use [[0] * 3] * 5, why?
    multilist = [[0 for col in range(5)] for row in range(10)]
    print multilist

### zip build in func
def zip_test():
    x = [1,2,3]
    y = [4,5,6]
    z = [7,8,9]
    zipped = zip(x,y,z)
    print zipped
    zipped_dict = dict(zip(x,y))
    print zipped_dict

### default value for dict
def init_or_add_dict():
    dic = {}
    dic.setdefault("aa",[]).append(123)

###
def union_intersection_dict():
    a = dict.fromkeys(range(10))
    b = dict.fromkeys(range(20,30))
    union = dict(a, **b)
    inter = dict.fromkeys([x for x in a if x in b])
    # or using set
    aset = set(range(10))
    bset = set(range(5,25))
    aunion = aset | bset
    ainter = aset & bset
    dict_con = dict.fromkeys(aunion)
    print aunion
    print ainter
    print dict_con

union_intersection_dict()
