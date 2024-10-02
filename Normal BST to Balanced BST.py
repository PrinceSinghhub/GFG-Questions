# User function Template for python3

class Solution:
    def buildBalancedTree(self, root):
        nodes = []
        self.inOrder(root, nodes)
        return self.buildTree(nodes, 0, len(nodes) - 1)

    def inOrder(self, root, nodes):
        if not root:
            return
        self.inOrder(root.left, nodes)
        nodes.append(root)
        self.inOrder(root.right, nodes)

    def buildTree(self, nodes, start, end):
        if start > end:
            return None
        mid = (start + end) // 2
        root = nodes[mid]
        root.left = self.buildTree(nodes, start, mid - 1)
        root.right = self.buildTree(nodes, mid + 1, end)
        return root


# {
# Driver Code Starts
# Initial Template for Python 3

# Initial Template for Python 3

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


def height(root):
    if (root == None):
        return 0;
    else:
        lDepth = height(root.left);
        rDepth = height(root.right);
        if (lDepth > rDepth):
            return (lDepth + 1);
        else:
            return (rDepth + 1);


if __name__ == "__main__":
    t = int(input())
    for _ in range(0, t):
        s = input()
        root = buildTree(s)
        ob = Solution()
        new = (ob.buildBalancedTree(root))
        print(height(new))

# } Driver Code Ends