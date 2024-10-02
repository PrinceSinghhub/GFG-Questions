'''
# Node Class:
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''
from collections import defaultdict
class Solution:
    
    def verticalSum(self, root):
      
       d=defaultdict(list)
       
       def helper(root,d,hd):
           if not root:
               return
           if hd in d:
               d[hd].append(root.data)
           else:
               d[hd].append(root.data)
           helper(root.left,d,hd-1)
           helper(root.right,d,hd+1)
       helper(root,d,0)
       ans=[]
      
       print(d)
      
       for i,j in sorted(d.items()):
           ans.append(j)
       print(ans)
       return ans  