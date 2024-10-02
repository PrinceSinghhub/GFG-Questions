'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''


class Solution:
    def leftsolve(self, root):
        if root:
            if root.left:
                self.stack.append(root.data)
                self.leftsolve(root.left)
            elif root.right:
                self.stack.append(root.data)
                self.leftsolve(root.right)

    def rightsolve(self, root):
        if root:
            if root.right:
                self.rightsolve(root.right)
                self.stack.append(root.data)
            elif root.left:
                self.rightsolve(root.left)
                self.stack.append(root.data)

    def leavessolve(self, root):
        if root:
            self.leavessolve(root.left)

            if (root.left is None) and (root.right is None):
                self.stack.append(root.data)

            self.leavessolve(root.right)

    def printBoundaryView(self, root):
        # Code here
        self.stack = []
        if root:
            self.stack.append(root.data)
            self.leftsolve(root.left)
            self.leavessolve(root.left)
            self.leavessolve(root.right)
            self.rightsolve(root.right)
        return self.stack