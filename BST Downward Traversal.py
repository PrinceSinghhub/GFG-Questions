class Solution:
    def dfs(self, root, targetValue, hasFound=False, targetPos=0, currPos=0):
        if root is None:
            return 0

        ans = 0
        if hasFound and targetPos == currPos:
            ans += root.data

        if not hasFound and root.data == targetValue:
            hasFound = True
            targetPos = currPos
            ans += 1

        ans += self.dfs(root.left, targetValue, hasFound, targetPos, currPos - 1)
        ans += self.dfs(root.right, targetValue, hasFound, targetPos, currPos + 1)
        return ans

    def verticallyDownBST(self, root, target):
        return self.dfs(root, target) - 1