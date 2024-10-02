from typing import List


class Solution:
    def getMaximum(self, N: int, arr: List[int]) -> int:
        # code here

        X = sum(arr)

        for i in range(N, 1, -1):

            if X % i == 0:
                return i

        return 1
