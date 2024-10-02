#User function Template for python3

class Solution:
   def checkBST(node,ftp,q,c):
       if ftp[0]==False:
           return
       if node is not None:
           if node.left is not None:
               Solution.checkBST(node.left,ftp,q,c)
           if q[0]<node.data:
               c[0]+=1
               q[0]=node.data
           else:
               ftp[0]=False
           if node.right is not None:
               Solution.checkBST(node.right,ftp,q,c)
   def largestBst(self, root):
       que=[root]
       max_size=1
       while bool(que):
           node=que.pop(0)
           ftp,c,q=[True],[0],[-1]
           Solution.checkBST(node,ftp,q,c)
           if ftp[0]==True:
               max_size=max(max_size,c[0])
           if node.left is not None:
               que.append(node.left)
           if node.right is not None:
               que.append(node.right)
       return max_size

#{
#  Driver Code Starts
import sys
sys.setrecursionlimit(1000000)

from collections import deque

# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

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
    while size > 0 and i < len(ip):
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
        ob = Solution()
        print(ob.largestBst(root))

# } Driver Code Ends