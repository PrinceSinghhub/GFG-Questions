#User function Template for python3

class Solution:
    def solve (self, L, R):
        
        count = 0
        for i in range(L,R+1):
            if bin(i)[2::].count('1') == 3:
                count+=1
        return count
  
    def precompute (self):
        pass



#{ 
 # Driver Code Starts
#Initial Template for Python 3


if __name__ == '__main__': 
    ob = Solution()
    ob.precompute()
    t = int (input ())
    for _ in range (t):
        L, R = map(int,input().split())
        ans = ob.solve(L, R);
        print(ans)




# } Driver Code Ends