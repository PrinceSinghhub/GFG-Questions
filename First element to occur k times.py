class Solution:
    def firstElementKTime(self, a, n, k):
        # code here
        from collections import defaultdict

        freq_map = defaultdict(int)

        for i in a:
            freq_map[i] += 1
            if (freq_map[i] == k):
                return i
        return -1

    # def firstElementKTime(self,  a, n, k):

    #     arr = [i for i in a if a.count(i) == k]
    #     arr.sort()
    #     return arr[0]

ans = Solution()
print(ans.firstElementKTime([1, 7, 4, 3, 4, 8, 7],7,2))