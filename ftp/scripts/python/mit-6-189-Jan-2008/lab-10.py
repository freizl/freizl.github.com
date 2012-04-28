#!/usr/bin/python

### Lab - 10
# only good for small inventory
# for giant inventory, it should be pre-defined by category

category = { "cheap" : lambda price: price < 20,
             "moderate" : lambda price: price >= 20 and price < 100,
             "expensive" : lambda price: price >= 100 }

inventory = { "hammer" : { "price" : 10, "count" : 100}
              ,"screw" : { "price" : 1, "count" : 1000}
              ,"nail" : { "price" : 1, "count" : 1000}
              ,"screwdriver" : { "price" : 8, "count" : 100}
              ,"drill" : { "price" : 50, "count" : 20}
              ,"workbench" : { "price" : 150, "count" : 5}
              ,"handsaw" : { "price" : 15, "count" : 50}
              ,"chainsaw" : { "price" : 80, "count" : 30} }

def get_items(cheapness):
    return [(name, (value["price"], value["count"])) for name, value in inventory.items() if category[cheapness](value["price"])]

# Testing
cheap = get_items("cheap")
print cheap
print type(cheap) is list
print len(cheap) == 5

moderate = get_items("moderate")
print moderate
print type(moderate) is list
print len(moderate) == 2

expensive = get_items("expensive")
print type(expensive) is list
print len(expensive) == 1

