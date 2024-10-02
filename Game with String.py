from collections import Counter
import heapq


class Solution:
    def minValue(self, s: str, k: int) -> int:
        maxheap = []
        char_count = Counter(s)

        for count in char_count.values():
            heapq.heappush(maxheap, -count)

        while k > 0:
            count = -heapq.heappop(maxheap)
            count -= 1
            k -= 1
            heapq.heappush(maxheap, -count)

        sum_of_squares = sum(count ** 2 for count in maxheap)
        return sum_of_squares