# User function Template for python3
class Solution:

    def nextGreatest(self, arr, n):

        ans = []

        for i in range(n):
            if i == len(arr) - 1:
                ans.append(-1)
            temp = arr[i + 1::]
            if len(temp) > 0:
                ans.append(max(temp))
        arr[:] = ans
        return arr

ans = Solution()
arr = [16, 17, 4, 3, 5, 2]
n = 6
print(ans.nextGreatest(arr,n))