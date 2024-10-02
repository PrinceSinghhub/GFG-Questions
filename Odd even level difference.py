'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''
class Solution:
    def getLevelDiff(self, root):
        # Code here
        sum1=0
        sum2=0
        i=0
        queue=[root]
        level=[]
        while queue!=[] and root is not None:
            l=[]
            for node in queue:
                l.append(node.data)
                if node.left:
                    level.append(node.left)
                if node.right:
                    level.append(node.right)
            if i%2==0:
                sum1+=sum(l)
            else:
                sum2+=sum(l)
            i+=1
            queue=level
            level=[]
        return sum1-sum2