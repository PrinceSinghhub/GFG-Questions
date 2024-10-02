# User function Template for python3


class Solution:
    def connect(self, root):
        if root is None:
            return None
        queue = []
        queue.append(root)
        while queue:
            extra = []
            for _ in range(len(queue)):
                temp = queue.pop(0)
                if temp.left:
                    if len(extra) != 0:
                        extra[-1].nextRight = temp.left
                    extra.append(temp.left)
                if temp.right:
                    if len(extra) != 0:
                        extra[-1].nextRight = temp.right
                    extra.append(temp.right)
            if len(extra) != 0:
                extra[-1].nextRight = None
            queue[:] = extra[:]


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
        self.nextRight = None


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


def InOrder(root):
    '''
    :param root: root of the given tree.
    :return: None, print the space separated in order Traversal of the given tree.
    '''
    if root is None:  # check if the root is none
        return
    InOrder(root.left)  # do in order of left child
    print(root.data, end=" ")  # print root of the given tree
    InOrder(root.right)  # do in order of right child


def printSpecial(root):
    leftmost_node = root

    while leftmost_node:
        curr_node = leftmost_node
        leftmost_node = None
        if curr_node.left:
            leftmost_node = curr_node.left
        elif curr_node.right:
            leftmost_node = curr_node.right

        print(curr_node.data, end=" ")
        while curr_node.nextRight:
            print(curr_node.nextRight.data, end=" ")
            curr_node = curr_node.nextRight
    print()


if __name__ == "__main__":
    t = int(input())
    for _ in range(0, t):
        s = input()
        root = buildTree(s)
        obj = Solution();
        obj.connect(root)
        printSpecial(root)
        InOrder(root)
        print()

# } Driver Code Ends