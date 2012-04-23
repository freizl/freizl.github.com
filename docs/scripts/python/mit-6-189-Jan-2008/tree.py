#!/usr/bin/python

### A tree data structure implementation

### Abstract data type: Tree
class Tree:
  def __init__(self, cargo, left=None, right=None):
    self.cargo = cargo
    self.left  = left
    self.right = right

  def __str__(self):
    return str(self.cargo) 

  # look the output sideways to see the tree structure
  def print_tree_indented(self, level=0):
      if self.right != None:
          self.right.print_tree_indented(level+1)
      print '  '*level + str(self.cargo)
      if self.left != None:
          self.left.print_tree_indented(level+1) 

if __name__ == '__main__':
    tree1 = Tree("+", Tree(2), Tree("*", Tree(3), Tree(4)))
    tree1.print_tree_indented()
