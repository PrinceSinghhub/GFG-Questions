from typing import List
import bisect
class Solution:
    def findLeastGreater(self, n : int, a : List[int]) -> List[int]:
        ans = [-1]
        temp = [a[n-1]]
        for i in range(n-2,-1,-1):
            k = bisect.bisect_right(temp,a[i])
            if k>=0 and k<len(temp):
                bisect.insort_left(temp,a[i])
                ans.append(temp[k+1])
            else:
                bisect.insort_left(temp,a[i])
                ans.append(-1)
        return ans[::-1]