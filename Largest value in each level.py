class Solution:
    def largestValues(self, root):
        #code here
        ans=[]
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
            ans.append(max(l))
            queue=level
            level=[]
        return ans
