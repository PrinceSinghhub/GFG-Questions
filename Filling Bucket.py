class Solution:

    def fillingBucket(self, N):
        # code here

        l = [0 for i in range(N + 1)]

        l[-1] = 1

        l[-2] = 1

        a = 10 ** 8

        for i in range(N - 2, 0 - 1, -1):
            l[i] = (l[i + 1] + l[i + 2]) % a

        return (l[0] % a)


# {
# Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())

        ob = Solution()
        print(ob.fillingBucket(N))
# } Driver Code Ends