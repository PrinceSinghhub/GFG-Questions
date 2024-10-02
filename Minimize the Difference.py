class Solution:
    def minimizeDifference(self, n, k, arr):
        post_max = [0] * n
        post_min = [0] * n
        post_max[-1] = post_min[-1] = arr[-1]

        for i in range(n - 2, -1, -1):
            post_max[i] = max(arr[i], post_max[i + 1])
            post_min[i] = min(arr[i], post_min[i + 1])

        mini = maxi = arr[0]
        res = post_max[k] - post_min[k]

        for i in range(1, n - k):
            res = min(res, max(maxi, post_max[i + k]) - min(mini, post_min[i + k]))
            mini = min(mini, arr[i])
            maxi = max(maxi, arr[i])

        res = min(res, maxi - mini)
        return res