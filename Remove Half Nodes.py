class Solution:
    def RemoveHalfNodes(self,root):
        if root:
            root.left=self.RemoveHalfNodes(root.left)
            root.right=self.RemoveHalfNodes(root.right)
            if ((not root.left) and (not root.right)) or (root.left and root.right):
                return root
            return root.left if root.left else root.right