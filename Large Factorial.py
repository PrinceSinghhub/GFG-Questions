import math


class Solution:

    def factorial(self, a, n):
        maximum = max(a)
        res = []
        dp = [1] * (maximum + 1)
        for i in range(1, maximum + 1):
            dp[i] = (i * dp[i - 1]) % 1000000007
        for val in a:
            res.append(dp[val])
        return res


# 	def factorial(self,a, n):
#     	# code here

#     	check = (10**9)+7

#     	ans = []

#     	for i in a:
#     	    res = int(math.factorial(i))
#     	    if res > check:
#     	        ans.append(res%check)
#     	    else:
#     	        ans.append(res)

#     	return ans


# {
#  Driver Code Starts
# Initial Template for Python 3


# Driver code
if __name__ == "__main__":
    tc = int(input())
    while tc > 0:
        n = int(input())
        a = list(map(int, input().strip().split()))
        ob = Solution()
        res = ob.factorial(a, n)
        for i in res:
            print(i, end=" ")
        print()
        tc = tc - 1

