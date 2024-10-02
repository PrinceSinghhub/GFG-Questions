import heapq
class Solution:
    def minOperations(self,a,n):
        # code here
        heap = []
        count = 0
        for i in range(n):
            if len(heap) != 0 and heap[0] < a[i]:
                count += a[i] - heap[0]
                heapq.heappush(heap,a[i])
                heapq.heappop(heap)
            heapq.heappush(heap,a[i])
        return count

ans = Solution()
arr = [3, 1, 2, 1]
print(ans.minOperations(arr))

