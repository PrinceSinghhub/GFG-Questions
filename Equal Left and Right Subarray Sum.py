class Solution:

    def equalSum(self, A, N):

        left_sum = 0
        right_sum = sum(A)

        for i in range(1, N + 1):
            right_sum -= A[i - 1]
            if left_sum == right_sum:
                return i
            left_sum += A[i - 1]

        return -1