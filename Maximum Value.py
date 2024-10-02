# {
# Driver Code Starts
# Initial Template for Python 3


from collections import deque
import sys

sys.setrecursionlimit(50000)


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


# } Driver Code Ends
# User function Template for python3
'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''


class Solution:
    def maximumValue(self, node):
        nodes_to_explore = deque()
        if not node:
            return 0

        level = 0
        lookup = dict()

        # Idea is to keep track of level along with the node itself
        # as we traverse the tree in BFS manner
        nodes_to_explore.append([level, node])

        while nodes_to_explore:
            cur_level, cur_node = nodes_to_explore.popleft()

            lookup[cur_level] = max(lookup.get(cur_level, float("-inf")), cur_node.data)
            # Use the current level to get next level when we push nodes for exploration, if any
            next_level = cur_level + 1

            if cur_node.left:
                nodes_to_explore.append([next_level, cur_node.left])
            if cur_node.right:
                nodes_to_explore.append([next_level, cur_node.right])

        return list(lookup.values())
        # code here


# {
# Driver Code Starts.
if __name__ == "__main__":
    t = int(input())
    for _ in range(0, t):
        s = input()
        root = buildTree(s)
        obj = Solution()
        ans = obj.maximumValue(root)
        for i in ans:
            print(i, end=' ')
        print();

# } Driver Code Ends