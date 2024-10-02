#User function Template for python3

class Solution():
    def no_of_subarrays(self, n,arr):
        #your code goes here
        result,c=0,0
        for i in arr:
            if(i==0):
                c+=1
            else:
                result+=((c*(c+1))//2)
                c=0
        if c!=0:
            result+=((c*(c+1))//2)
        return result


#{
 # Driver Code Starts
#Initial Template for Python 3


for _ in range(int(input())):
    n = int(input())
    arr = [int(i) for i in input().split()]
    print(Solution().no_of_subarrays(n, arr))
# } Driver Code Ends