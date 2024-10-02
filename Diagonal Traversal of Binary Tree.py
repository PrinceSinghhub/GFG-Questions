'''
# Node Class:
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
'''
#Complete the function below
class Solution:
    def preorder(self, node, d, l):
        if not node:
            return
        d[l].append(node.data)
        self.preorder(node.left, d, l+1)
        self.preorder(node.right, d, l)
    def diagonal(self,root):
        from collections import defaultdict
        d = defaultdict(list)
        self.preorder(root, d, 0)

        ans = []
        for k in sorted(d.keys()):
            for i in d[k]:
                ans.append(i)
        return ans