class Solution:
    def getCount(self, S, N):

        # char = []

        # for i in S:
        #     if i not in char and S.count(i) == N:
        #         char.append(i)

        # return len(char)
        A = [0] * 26
        A[ord(S[0]) - ord("a")] = 1
        for i in range(1, len(S)):

            if S[i] != S[i - 1]:
                A[ord(S[i]) - ord("a")] = A[ord(S[i]) - ord("a")] + 1

        count = A.count(N)

        return count


# {
#  Driver Code Starts
# Initial Template for Python 3

t = int(input())
for tc in range(t):
    s, n = input().split()
    s = str(s)
    n = int(n)
    ob = Solution()
    print(ob.getCount(s, n))