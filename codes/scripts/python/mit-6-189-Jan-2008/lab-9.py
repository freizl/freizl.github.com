#!/usr/bin/python

### Lab - 9

# problem 1

NAMES = ["Alice", "Bob", "Cathy", "Dan", "Ed", "Frank", "Gary", "Helen", "Irene", "Jack", "Kelly", "Larry"]
AGES = [20, 21, 18, 18, 19, 20, 20, 19, 19, 19, 22, 19]
peoples = zip(NAMES, AGES)

def peoples_at_age(age):
    return [p_name for p_name, p_age in peoples if p_age == age]

print peoples_at_age(19)
