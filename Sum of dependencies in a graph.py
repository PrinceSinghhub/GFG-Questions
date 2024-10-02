class Solution:
    def sumOfDependencies(self,adj,V):

        sum=0
        for i in adj:
            sum=sum+len(i)
        return sum