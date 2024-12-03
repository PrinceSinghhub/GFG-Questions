class Solution:
    def treePathSum(self, root):
        def preOrderTraversal(node, currentNumber):
            if not node:
                return 0
            currentNumber = currentNumber * 10 + node.data
            if not node.left and not node.right:
                return currentNumber
            return preOrderTraversal(node.left, currentNumber) + preOrderTraversal(node.right, currentNumber)

        return preOrderTraversal(root, 0)