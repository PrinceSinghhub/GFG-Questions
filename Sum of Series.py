class Solution:

    def seriesSum(self, n):
        ans = n * (n + 1) // 2

    return (ans)

    # ans = [i for i in range(1,n+1)]
    # return sum(ans)


# {
#  Driver Code Starts
# Initial Template for Python 3


# Driver code
if __name__ == "__main__":
    tc = int(input())
    while tc > 0:
        n = int(input())
        ob = Solution()
        ans = ob.seriesSum(n)
        print(ans)
        tc = tc - 1