import bisect


# Function to find a continuous sub-array which adds up to a given number.
class Solution:

    def subarraySum(self,arr, n, s):
        pre = [0] * (n + 1)
        for i in range(1, n + 1):
            pre[i] = pre[i - 1] + arr[i - 1]

        for i in range(1, n + 1):
            idx = bisect.bisect_left(pre, pre[i] - s, 0, i)
            if pre[i] - pre[idx] == s and idx != i:
                return [idx + 1, i]

        return [-1]