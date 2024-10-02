# User function Template for python3
class Solution:
    def lenOfLongSubarr(self, arr, n, k):
        total = 0
        hmap = {0: -1}
        ans = 0
        for idx, ele in enumerate(arr):
            total += ele
            if total not in hmap:
                hmap[total] = idx
            if total - k in hmap:
                ans = max(ans, idx - hmap[total - k])
        return ans
        # Complete the function


# {
# Driver Code Starts
# Initial Template for Python 3


for _ in range(0, int(input())):
    n, k = map(int, input().split())
    arr = list(map(int, input().strip().split()))
    ob = Solution()
    print(ob.lenOfLongSubarr(arr, n, k))

# } Driver Code Ends