class Solution:
    def buildTree(self, inorder, postorder, n):
        if n == 0:
            return None

        root = Node(postorder[n - 1])
        idx = inorder.index(postorder[n - 1])

        root.left = self.buildTree(inorder[:idx], postorder[:idx], idx)
        root.right = self.buildTree(inorder[idx + 1:], postorder[idx:-1], n - idx - 1)

        return root