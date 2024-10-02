class Solution:
    def canReach(self, A, N):
        # code here

        l = N - 1
        for i in range(N - 1, -1, -1):
            if i + A[i] >= l:
                l = i
        if l == 0:
            return 1
        return 0