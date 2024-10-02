# User function Template for python3

'''
class Node:
    def __init__(self,val):
        self.data=val
        self.left=None
        self.right=None
'''


class Solution:
    def maxDifferenceBST(self, root, target):
        def result(root):
            if root == None:
                return 1e9
            if root.left == None and root.right == None:
                return root.data
            l = result(root.left)
            r = result(root.right)
            return min(l, r) + root.data

        val = [0]

        def solve(root, t):
            if root == None:
                return -1
            if root.data == t:
                val[0] = min(result(root.left), result(root.right))
                return 0

            if root.data > t:
                ans = solve(root.left, t)
            else:
                ans = solve(root.right, t)
            if ans != -1:
                return ans + root.data
            else:
                return -1

        res = solve(root, target)
        if val[0] == 1e9:
            return res
        return res - val[0]


# {
# Driver Code Starts
# Initial Template for Python 3
class Node:
    """ Class Node """

    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None


class Tree:
    def createNode(self, data):
        return Node(data)

    def insert(self, node, data):
        if node is None:
            return self.createNode(data)
        else:
            if data < node.data:
                node.left = self.insert(node.left, data)
            else:
                node.right = self.insert(node.right, data)
            return node

    def traverseInorder(self, root):
        if root is not None:
            print(root.data, end=" ")
            self.traverseInorder(root.left)
            self.traverseInorder(root.right)


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = input().strip().split()
        root = None
        tree = Tree()
        root = tree.insert(root, int(arr[0]))
        for j in range(1, n):
            root = tree.insert(root, int(arr[j]))
        # tree.traverseInorder(root)
        target = int(input())

        res = Solution().maxDifferenceBST(root, target)
        print(res)

# } Driver Code Ends