class Solution:
    def minTime(self, root, target):
        graph = {}
        S = set()

        def dfs(root, parent):
            if not root:
                return
            # if root not in graph:
            graph[root.data] = []
            S.add(root.data)
            if parent:
                graph[root.data].append(parent.data)
            if root.left:
                graph[root.data].append(root.left.data)
            if root.right:
                graph[root.data].append(root.right.data)
            dfs(root.left, root)
            dfs(root.right, root)

        dfs(root, None)
        time = 0
        Q, neighbours = [target], []
        while True:
            time += 1
            while Q:
                element = Q.pop()
                for n in graph[element]:
                    if n in S:
                        neighbours.append(n)
                S.remove(element)
            if not neighbours:
                break
            while neighbours:
                Q.append(neighbours.pop())
        return time - 1


# {
#  Driver Code Starts
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


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        line = input()
        target = int(input())
        root = buildTree(line)
        print(Solution().minTime(root, target))

# } Driver Code Ends