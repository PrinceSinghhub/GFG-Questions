# User function Template for python3

'''
# Node Class:
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''


class Solution:
    def pathtoNode(self, root, n, path):
        if root is None:
            return False
        # append the current node to the given path
        path.append(root.data)
        # if current value is equal to the path return True
        if root.data == n:
            return True
        # checking for left and right part of the tree
        if ((root.left != None and self.pathtoNode(root.left, n, path)) or
                (root.right != None and self.pathtoNode(root.right, n, path))):
            return True
        # once covered the path pop that path from the given path
        path.pop()
        return False

    def findDist(self, root, a, b):
        if root:
            path1 = []
            self.pathtoNode(root, a, path1)
            path2 = []
            self.pathtoNode(root, b, path2)

            # print(path1)
            # print(path2)
            # check for the value at which the two paths intersect
            i = 0
            while i < len(path1) and i < len(path2):
                if path1[i] != path2[i]:
                    break
                i += 1
            # return the sum of the lenght of the path since I am considering the value
            # twice so we need to remove it the path
            return (len(path1) + len(path2) - 2 * i)
        else:
            return 0


# {
#  Driver Code Starts
# Initial Template for Python 3

import sys

sys.setrecursionlimit(50000)
from collections import deque


# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None


'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''


# Function to Build Tree
def buildTree(s):
    # Corner Case
    if (len(s) == 0 or s[0] == "N"):
        return None

    # Creating list of strings from input
    # string after spliting by space
    ip = list(map(str, s.split()))

    # Create the root of the tree
    root = Node(int(ip[0]))
    size = 0
    q = deque()

    # Push the root to the queue
    q.append(root)
    size = size + 1

    # Starting from the second element
    i = 1
    while (size > 0 and i < len(ip)):
        # Get and remove the front of the queue
        currNode = q[0]
        q.popleft()
        size = size - 1

        # Get the current node's value from the string
        currVal = ip[i]

        # If the left child is not null
        if (currVal != "N"):
            # Create the left child for the current node
            currNode.left = Node(int(currVal))

            # Push it to the queue
            q.append(currNode.left)
            size = size + 1
        # For the right child
        i = i + 1
        if (i >= len(ip)):
            break
        currVal = ip[i]

        # If the right child is not null
        if (currVal != "N"):
            # Create the right child for the current node
            currNode.right = Node(int(currVal))

            # Push it to the queue
            q.append(currNode.right)
            size = size + 1
        i = i + 1
    return root


if __name__ == "__main__":
    t = int(input())
    for _ in range(0, t):
        s = input()
        root = buildTree(s)
        a, b = map(int, input().split())
        ob = Solution()
        print(ob.findDist(root, a, b))

# } Driver Code Ends