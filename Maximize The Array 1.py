import heapq


class Solution:
    def maximizeArray(self, arr1, arr2, n):
        heap = []
        heapq.heapify(heap)
        for i in range(n):
            heapq.heappush(heap, (-arr2[i], 0, i))
            heapq.heappush(heap, (-arr1[i], 1, i))
        i1 = []
        i2 = []
        used = set()
        k = 0
        while k < n and heap:
            ele, ar, ind = heapq.heappop(heap)
            if ar == 1 and ele not in used:
                i1.append(ind)
                used.add(ele)
                k += 1
            elif ar == 0 and ele not in used:
                i2.append(ind)
                used.add(ele)
                k += 1

        i1.sort()
        i2.sort()
        ans = []
        for i in i2:
            ans.append(arr2[i])
        for i in i1:
            ans.append(arr1[i])
        return ans