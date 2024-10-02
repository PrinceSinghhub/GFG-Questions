class Solution:
    def parent(self,root,d,target):
        queue=[]
        d[root]=None
        queue.append(root)
        while(queue):
            node=queue.pop(0)
            if node.left:
                d[node.left]=node
                queue.append(node.left)
            if node.right:
                d[node.right]=node
                queue.append(node.right)
            if node.data==target:
                tar=node
        return tar
                
    def KDistanceNodes(self,root,target,k):
        d={}
        tar=self.parent(root,d,target)
        visited={}
        queue1=[]
        queue1.append(tar)
        visited[tar]=True
        distance=0
        while(queue1):
            n=len(queue1)
            if distance==k:
                break
            else:
                distance+=1
            for i in range(n):
                curr=queue1.pop(0)
                if curr.left and curr.left not in visited :
                    queue1.append(curr.left)
                    visited[curr.left]=True
                if curr.right and curr.right not in visited :
                    queue1.append(curr.right)
                    visited[curr.right]=True
                if d[curr] and d[curr] not in visited:
                    queue1.append(d[curr])
                    visited[d[curr]]=True
            
        res=[]
        while(queue1):
            curr=queue1.pop(0)
            res.append(curr.data)
        res.sort()
        return res

#{ 
 # Driver Code Starts
#Initial Template for Python 3

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
    x = Solution()
    t = int(input())
    for _ in range(t):
        line = input()
        target=int(input())
        k=int(input())

        root = buildTree(line)
        res = x.KDistanceNodes(root,target,k)
        
        for i in res:
            print(i, end=' ')
        print()

# } Driver Code Ends