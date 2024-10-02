class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None


class Solution:
    def maxDepth(self, root):
        if root == None:
            return 0

        lh = self.maxDepth(root.left)
        rh = self.maxDepth(root.right)

        return 1 + max(lh,rh)
