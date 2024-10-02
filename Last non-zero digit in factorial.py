#User function Template for python3

import math
class Solution:
    def lastNon0Digit (self, N):
        
        n = str(int((math.factorial(N))))
        
        for i in n[::-1]:
            if int(i) != 0:
                return int(i)
                
        
        



#{ 
 # Driver Code Starts
#Initial Template for Python 3



if __name__ == '__main__': 
    ob = Solution()
    t = int (input ())
    for _ in range (t):
        N = int(input())
        ans = ob.lastNon0Digit(N);
        print(ans)




# } Driver Code Ends