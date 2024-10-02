class Solution:

    def isvalid(self, arr, n, k, mid):
        student = 1
        summ = 0
        for i in range(n):
            summ += arr[i]
            if summ > mid:
                student += 1
                summ = arr[i]
        if student > k:
            return False
        return True

    def findPages(self, A, n, k):
        if n < k:
            return -1
        start = max(A)
        end = sum(A)

        self.res = -1

        while start <= end:
            mid = start + (end - start) // 2
            if self.isvalid(A, n, k, mid):
                self.res = mid
                end = mid - 1
            else:
                start = mid + 1

        return self.res

ans = Solution()
n = 4
arr = [12,34,67,90]
m = 2
print(ans.findPages(arr,n,m))