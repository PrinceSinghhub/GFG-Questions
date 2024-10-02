class Solution:
    def __init__(self):
        self.ans = 0
        self.k = 0
        self.sum = 0
        self.mp = {}

    def rec(self, root):
        if not root:
            return
        self.sum += root.data
        self.ans += self.mp.get(self.sum - self.k, 0)
        self.mp[self.sum] = self.mp.get(self.sum, 0) + 1
        self.rec(root.left)
        self.rec(root.right)
        self.mp[self.sum] -= 1
        if self.mp[self.sum] == 0:
            del self.mp[self.sum]
        self.sum -= root.data

    def sumK(self, root, K):
        self.ans = 0
        self.k = K
        self.sum = 0
        self.mp = {0: 1}
        self.rec(root)
        return self.ans