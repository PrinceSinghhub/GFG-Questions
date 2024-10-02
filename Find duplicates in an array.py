from collections import Counter


class Solution:
    def duplicates(self, arr, n):
        # code here

        mydic = Counter(arr)
        ans = []

        for key, value in mydic.items():
            if value > 1:
                ans.append(key)

        if len(ans) == 0:
            return [-1]
        ans.sort()
        return ans


# {
#  Driver Code Starts
if (__name__ == '__main__'):
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        res = Solution().duplicates(arr, n)
        for i in res:
            print(i, end=" ")
        print()