class Solution:

    def findMaxSum(self,arr, n):

        for i in range(2,n):

            if i-3>=0:

                t=max(arr[i-2],arr[i-3])

            else:

                t=arr[i-2]

            arr[i]+=t

        return(max(arr[n-2:]))

#{
 # Driver Code Starts
#Initial Template for Python 3




if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.findMaxSum(arr, n)
        print(ans)
        tc -= 1

# } Driver Code Ends