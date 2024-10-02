# User function Template for python3

class Solution:
    def getMinDiff(self, arr, n, k):

        arr.sort()
        n = len(arr)
        maxx = 0
        minn = 0
        diff = arr[n - 1] - arr[0]

        for i in range(0, len(arr)):
            if arr[i] < k:
                continue
            maxx = max(arr[i - 1] + k, arr[n - 1] - k)
            minn = min(arr[0] + k, arr[i] - k)
            diff = min(diff, abs(maxx - minn))
        return diff


# {
# Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        k = int(input())
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.getMinDiff(arr, n, k)
        print(ans)
        tc -= 1

# } Driver Code Ends