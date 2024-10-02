from typing import List

class Solution:
    def longestSubseq(self, n: int, nums: List[int]) -> int:
        mp = {}
        ans = 0
        for num in nums:
            left = mp.get(num - 1, 0)
            right = mp.get(num + 1, 0)
            mp[num] = 1 + max(left, right)
            ans = max(ans, mp[num])
        return ans
