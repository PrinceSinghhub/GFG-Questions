from typing import List

class Solution:
    def findMaxSubsetSum(self, N : int, a : List[int]) -> int:
        # code here
        take = 0
        Untake=0
        for i in a:
            take,Untake=max(i+take,Untake),i+take
        return max(take,Untake)
