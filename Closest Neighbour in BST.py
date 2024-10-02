class Solution:
    def findMaxForN(self, root, n):
        ans=None
        while root:
            if root.key>n:
                root=root.left
            else:
                ans=root.key
                root=root.right
        return ans if ans else -1