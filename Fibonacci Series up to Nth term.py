#User function Template for python3

class Solution:
    
    def findans(self,n,ans):
        
        if n == 0 or n == 1:
            return ans
        
        self.findans(n-1,ans)
        ans.append(ans[n-1]+ans[n-2])
        return ans

    
    def series(self, n):
        
        ans = [0,1]
        
        self.findans(n,ans)
        return ans
    
    # itreative approch
    '''def series(self, n):
        ans = []
        
        first = 0
        second = 1
        third = 0
        
        for i in range(n+1):
            ans.append(third)
            first = second
            second = third
            third = first+second
        
        return ans'''


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        result = ob.series(N)
        print(*result)
# } Driver Code Ends