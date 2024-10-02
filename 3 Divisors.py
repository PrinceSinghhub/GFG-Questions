import math
class Solution:
    def threeDivisors(self, query, q):
        # code here
        n = math.floor(math.sqrt(max(query)))
        prime = [True] * (n + 1)
        prime[0] = prime[1] = False
        for i in range(2, n + 1):
            if prime[i]:
                for j in range(i * i, n + 1, i):
                    prime[j] = False
        dp = [0] * (n + 1)
        for i in range(2, n + 1):
            dp[i] = dp[i - 1]
            if prime[i]:
                dp[i] += 1
        ans = []
        for i in query:
            val = math.floor(math.sqrt(i))
            ans.append(dp[val])
        return ans


# {
# Driver Code Starts
# Initial Template for Python 3


if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        q = int(input())
        query = []
        for _ in range(q):
            query.append(int(input()))

        ob = Solution()
        ans = ob.threeDivisors(query, q)
        for a in ans:
            print(a)

# } Driver Code Ends