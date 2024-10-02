import sys
def convert_expression(expression, i):
    pass



sys.setrecursionlimit(10000)

class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None


# Function to print the tree
# in a pre-order traversal pattern
def print_tree(root):
    if not root:
        return
    print(root.data, end=' ')

s = "a?b?c:d:e"
res = ""
for i in s:
    if i.isalpha():
        res+=i
        res+=" "
print(res)