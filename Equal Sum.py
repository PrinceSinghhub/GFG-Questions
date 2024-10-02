# User function Template for python3
class Solution:
    def equilibrium(self, arr, n):
        # code here
        lsum = a[0]
        rsum = 0
        for k in range(2, len(arr)):
            rsum = rsum + arr[k]
            for i in range(1, len(a) - 1):
                if (lsum == rsum):
                    return "YES"
                else:
                    rsum = rsum - a[i + 1]
                    lsum = lsum + a[i]
        return "NO"


# {
#  Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':

    tc = int(input())
    while tc > 0:
        n = int(input())
        a = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.equilibrium(a, n)
        print(ans)
        tc = tc - 1
# } Driver Code Ends