from heapq import heapify, heappop


class Solution:
    def totalWays(self, n, c):
        heapify(c)

        ans = 1
        z = 0
        for i in range(len(c)):
            val = heappop(c)
            ans *= (val - z)
            ans %= (10 ** 9 + 7)
            z += 1
        return ans % (10 ** 9 + 7)


# {
# Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        n = int(input())
        capacity = list(map(int, input().split()))
        ob = Solution()
        ans = ob.totalWays(n, capacity)
        print(ans)

# } Driver Code Ends