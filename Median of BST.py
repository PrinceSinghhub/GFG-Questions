# User function Template for python3
import math


def inorder(root):
    global arr
    if not root:
        return
    inorder(root.left)
    arr.append(root.data)
    inorder(root.right)


def findMedian(root):
    global arr
    arr = []
    inorder(root)
    # print(arr)

    m = int(len(arr) / 2)
    n = len(arr)
    if n % 2 == 0:
        ans = (arr[m] + arr[m - 1]) / 2
        if math.floor(ans) == math.ceil(ans):
            return int(ans)
        else:
            return ans
    else:
        return arr[m]


# {
# Driver Code Starts
# Initial Template for Python 3

from collections import deque


class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None


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
    for _ in range(t):
        s = input()
        root = buildTree(s)
        print(findMedian(root))

# } Driver Code Ends