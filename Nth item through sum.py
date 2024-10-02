class Solution:
    def nthItem(self, L1, L2, A, B, N):
        arr = sorted({i + j for i in B for j in A})

        if N > len(arr):
            return -1

        return arr[N - 1]