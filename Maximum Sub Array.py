class Solution:
    def findSubarray(self, a):
        n = len(a)
        flag = 0
        for i in range(n):
            if a[i] >= 0:
                flag = 1
        if flag == 0:
            return [-1]
        sum_prev, sum_curr, l, l1, r = 0, 0, 0, 0, 0
        for i in range(n):
            if a[i] >= 0:
                sum_curr += a[i]
            if (a[i] < 0 or i == n - 1):
                if (sum_curr > sum_prev) or (sum_prev == sum_curr and (i - l1 + 1) > (r - l)):
                    sum_prev = sum_curr
                    r = i
                    l = l1
                    if (i == n - 1 and a[i] >= 0):
                        r += 1
                l1 = i + 1
                sum_curr = 0
        return a[l:r]

arr = [1,1,2,4,8]
ans = Solution()
print(ans.findSubarray(arr))