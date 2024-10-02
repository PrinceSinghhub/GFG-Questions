
'''
# Node Class:
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''
class Solution:
    def verticalSum(self, root):
      
       d={}
       
       def helper(root,d,hd):
           if not root:
               return
           if hd in d:
               d[hd]=d[hd]+root.data
           else:
               d[hd]=root.data
           helper(root.left,d,hd-1)
           helper(root.right,d,hd+1)
       helper(root,d,0)
       ans=[]
       for i,j in sorted(d.items()):
           ans.append(j)
       return ans  