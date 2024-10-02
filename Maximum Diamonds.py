import bisect


class Solution:

    def maxDiamonds(self, A, N, K):
        c = 0

        s = 0

        A.sort()

        while c != K:
            a = A[-1]

            A.pop()

            s += a

            bisect.insort(A, a // 2)

            c += 1

        return s


# {
# Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N, K = map(int, input().split())
        A = list(map(int, input().split()))

        ob = Solution()
        print(ob.maxDiamonds(A, N, K))
# } Driver Code Ends