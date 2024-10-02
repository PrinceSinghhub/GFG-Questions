class Solution:
    def isBalanced(self, root):
        h, isRootBalanced = self.isBalanced_improved(root)
        return isRootBalanced

    def isBalanced_improved(self, root):  # todo O(N) revise dry run and understand
        if root is None:
            return 0, True
        lh, isleftBlanced = self.isBalanced_improved(root.left)
        rh, isrightBalanced = self.isBalanced_improved(root.right)

        h = 1 + max(lh, rh)
        if abs(lh - rh) > 1:
            return h, False

        if isleftBlanced and isrightBalanced:
            return h, True
        else:
            return h, False