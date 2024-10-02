class Solution:
    def totalCount(self, arr, n, k):

        ans = 0

        for i in arr:
            if i == 0:
                ans += 1

            elif i % k == 0:
                ans += (i // k)
            else:
                ans += (i // k) + 1

        return ans


# {
#  Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, k = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.totalCount(arr, n, k)
        print(ans)
        tc -= 1