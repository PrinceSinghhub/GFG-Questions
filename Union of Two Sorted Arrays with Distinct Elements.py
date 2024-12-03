class Solution:
    #Function to return a list containing the union of the two arrays.
    def findUnion(self,a,b):
        c=set(a)
        d=set(b)
        return sorted(c.union(d))