class Solution:

    def topK(self, nums, k):

        # Code here
        count = dict()
        for i in nums:
            if i not in count:
                count[i] = 1
            else:
                count[i] += 1

        return sorted(count, key=lambda item: (count[item], item), reverse=True)[:k]

ans = Solution()
print(ans.topK([1,1,1,2,2,3],6))