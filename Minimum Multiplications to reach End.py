from queue import Queue
import sys


class Solution:
    def __init__(self):
        self.MOD = 100000

    def minimumMultiplications(self, arr, start, end):
        if start == end:
            return 0

        q = Queue()
        q.put(start)

        mind = [sys.maxsize] * self.MOD
        mind[start] = 0

        while not q.empty():
            s = q.get()
            for i in range(len(arr)):
                x = (arr[i] * s) % self.MOD
                if mind[x] > mind[s] + 1:
                    mind[x] = mind[s] + 1
                    q.put(x)
                    if x == end:
                        return mind[x]

        return -1


# Example usage:
solution = Solution()
arr = [2, 3, 5]
start = 2
end = 10
result = solution.minimumMultiplications(arr, start, end)
print(result)  # This will print the minimum number of multiplications to reach 'end' from 'start'.
