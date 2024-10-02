from collections import deque


class Solution:
    def partitionArray(self, N, K, M, arr):

        arr.sort()
        dequ = deque([0])

        for i in range(K - 1, N):
            while i - dequ[0] + 1 >= K:
                if arr[i] - arr[dequ[0]] <= M:
                    dequ.append(i + 1)
                    break
                dequ.popleft()
                if not dequ:
                    return False

        return dequ[-1] == N