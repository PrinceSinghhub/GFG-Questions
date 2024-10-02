class Solution:
    def buildtree(self, inorder, preorder, n):
        self.preorderIter = 0
        return self.buildtreeUtil(inorder, preorder, 0, n - 1)

    def buildtreeUtil(self, inorder, preorder, start, end):
        if start > end:
            return None
        node = Node(preorder[self.preorderIter])
        inorderIndex = start + inorder[start:end + 1].index(preorder[self.preorderIter])
        self.preorderIter += 1
        node.left = self.buildtreeUtil(inorder, preorder, start, inorderIndex - 1)
        node.right = self.buildtreeUtil(inorder, preorder, inorderIndex + 1, end)
        return node
