from typing import List


class Solution:
    def minimumSwaps(self, c: List[int], v: List[int], n: int, k: int, b: int, t: int) -> int:
        # code here
        good, bad, swap = 0, 0, 0
        for i in range(n - 1, -1, -1):
            if c[i] + v[i] * t >= b:
                good += 1
                swap += bad
            else:
                bad += 1

            if good >= k:
                break

        if good >= k:
            return swap
        return -1