# User function Template for python3

'''
# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

'''


class Solution:
    # Function for the inorder traversal of the tree
    # so as to store the node values in 'arr' in
    # sorted order
    def inorderTraversal(self, root, arr):

        if (root == None):
            return arr

        # first recur on left subtree
        self.inorderTraversal(root.left, arr)

        # then copy the data of the node
        arr.append(root.data)

        # now recur for right subtree
        self.inorderTraversal(root.right, arr)

        return arr

    def BSTToMaxHeap(self, root, arr):

        global i
        if (root == None):
            return None

        # recur on left subtree
        root.left = self.BSTToMaxHeap(root.left, arr)

        # recur on right subtree
        root.right = self.BSTToMaxHeap(root.right, arr)

        # copy data at index 'i' of 'arr' to
        # the node
        root.data = arr[i]
        i = i + 1
        return root

    # Utility function to convert the given BST to
    # MAX HEAP
    def convertToMaxHeapUtil(self, root):
        global i

        # vector to store the data of all the
        # nodes of the BST
        i = 0
        arr = []

        # inorder traversal to populate 'arr'
        arr = self.inorderTraversal(root, arr)

        # BST to MAX HEAP conversion
        root = self.BSTToMaxHeap(root, arr)


# {
#  Driver Code Starts
# Initial Template for Python

from collections import deque


# Tree Node
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


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


def postOrder(root):
    if root == None:
        return

    postOrder(root.left)
    postOrder(root.right)
    print(root.data, end=" ")


if __name__ == "__main__":
    t = int(input())
    for _ in range(0, t):
        s = input()
        root = buildTree(s)
        ob = Solution()

        ob.convertToMaxHeapUtil(root)
        postOrder(root)

        print()

# } Driver Code Ends