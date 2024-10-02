class Solution:
    def findans(self, index, n, arr, Sum, myans, check):
        if index >= n:
            if sum(myans) == Sum:
                check.append(1)
                return
            return

        myans.append(arr[index])
        self.findans(index + 1, n, arr, Sum, myans, check)
        myans.remove(arr[index])
        self.findans(index + 1, n, arr, Sum, myans, check),

    def isSubsetSum(self, N, arr, Sum):

        check = []
        self.findans(0, N, arr, Sum, [], check)
        # print(check)
        if sum(check) > 0:
            return True
        return False

    # dp Solution


class Solution:
    def isSubsetSum(self, n, arr, target):
        # code here
        dp = [[0] * (target + 1) for i in range(n)]
        for i in range(n):
            dp[i][0] = True
        if (arr[0] <= target):
            dp[0][arr[0]] = True
        for i in range(1, n):
            for tg in range(1, target + 1):
                nt = dp[i - 1][tg]
                t = False
                if target >= arr[i]:
                    t = dp[i - 1][tg - arr[i]]
                dp[i][tg] = nt or t
        return dp[n - 1][target]