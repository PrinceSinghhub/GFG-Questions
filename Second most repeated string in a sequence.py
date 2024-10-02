class Solution:
    def secFrequent(self, arr):

        mydic = {}

        for i in arr:
            if i in mydic:
                mydic[i]+=1

            else:
                mydic[i] = 1

        # print(mydic)
        value = list(mydic.values())
        value.sort()

        for key, val in mydic.items():
            if val == value[-2]:
                return key

ans = Solution()
arr = ['aaa', 'bbb', 'ccc', 'bbb', 'aaa', 'aaa']
print(ans.secFrequent(arr))
