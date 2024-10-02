class Solution:
    # Your task is to complete this function
    # Function should return an integer
    def countPS(self,string):
       dp = {}
       MOD = 10 ** 9 + 7
       def rec(i, j):
           if i > j:
               return 0
           if i == j:
               return 1
           if (i, j) in dp:
               return dp[(i, j)]
           if string[i] == string[j]:
               dp[(i, j)] = (1 + rec(i+1, j) + rec(i, j-1)) % MOD
               return dp[(i, j)]
           dp[(i, j)] = (MOD + rec(i+1, j) + rec(i, j-1) - rec(i+1, j-1)) % MOD
           return dp[(i, j)]
       return rec(0,len(string)-1)



#{
 # Driver Code Starts
#Initial template for Python 3

import sys
sys.setrecursionlimit(10**6)

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        ob=Solution()
        print(ob.countPS(input().strip()))

# } Driver Code Ends