class Solution:

    def maxGroupSize(self, arr, N, K):

        if N == 1:
            return 1

        l = [0] * K

        for i in arr:
            l[i % K] += 1

        c = 0

        if l[0] > 0:
            c += 1

        d = (K + 1) // 2

        for i in range(1, d):
            c += max(l[i], l[K - i])

        if K % 2 == 0 and l[K // 2] > 0:
            c += 1

            pass

        return c


# {
# Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N, K = map(int, input().split())
        arr = list(map(int, input().split()))

        ob = Solution()
        print(ob.maxGroupSize(arr, N, K))
# } Driver Code Ends