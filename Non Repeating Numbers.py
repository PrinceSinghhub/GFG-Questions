class Solution:
    def singleNumber(self, nums):

        mydic = {}

        for i in nums:
            if i not in mydic:
                mydic[i] = 1
            else:
                mydic[i] += 1

        ans = []

        for key, val in mydic.items():
            if val == 1:
                ans.append(key)

        ans.sort()
        return ans