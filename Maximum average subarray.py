class Solution:
    def findMaxAverage(self, arr, n, k):
        # code here
        ans = []

        for i in range(n - k+1):
            sub = arr[i:k+i]
            ans.append(sub)

        print(ans)

        finans = []
        Max = -9999999999999999999999
        for i in ans:
            if sum(i) > Max:
                Max = sum(i)
                finans[:] = i

        print(finans)


ans = Solution()
arr = [3, -435, 335, 10, -50, 100, 20]
k = 3
n = 7
print(ans.findMaxAverage(arr,n,k))