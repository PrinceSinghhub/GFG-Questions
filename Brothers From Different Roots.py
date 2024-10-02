class Solution:
    def countPairs(self, root1, root2, x):
        # code here.
        req = dict()

        def dfs1(node):
            if node:
                dfs1(node.left)
                req[x - node.data] = 1
                dfs1(node.right)

        dfs1(root1)
        ans = 0

        def dfs2(node):
            nonlocal ans
            if node:
                dfs2(node.left)
                if node.data in req:
                    ans += 1
                dfs2(node.right)

        dfs2(root2)

        return ans