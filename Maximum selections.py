class Solution:

    def max_non_overlapping(self, ranges):

        ranges.sort(key=lambda x: x[1])
        prev = -1
        count = 0
        for i in range(n):
            if ranges[i][0] >= prev:
                count += 1
                prev = ranges[i][1]
        return count

ans = Solution()
N = 4
print(ans.max_non_overlapping(N))