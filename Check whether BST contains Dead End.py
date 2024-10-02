class Solution:
    def isDeadEnd(self, root):
        def deadEnd(root, min_val, max_val):
            if not root:
                return False
            if min_val == max_val:
                return True
            return deadEnd(root.left, min_val, root.data - 1) or deadEnd(root.right, root.data + 1, max_val)
        return deadEnd(root, 1, float('inf'))