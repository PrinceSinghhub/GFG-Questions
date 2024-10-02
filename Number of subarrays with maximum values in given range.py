# User function Template for python3

class Solution:
    def countSubarrays(self, a, n, L, R):
        start, end, empire, ans = 0, 0, 0, 0
        for end in range(0, n):
            if a[end] >= L and a[end] <= R:
                empire = end - start + 1
            if a[end] > R:
                empire = 0
                start = end + 1
            ans += empire
        return ans


# {
# Driver Code Starts
# Initial Template for Python 3


for _ in range(0, int(input())):
    n, l, r = map(int, input().strip().split())
    arr = list(map(int, input().strip().split()))
    ob = Solution()
    v = ob.countSubarrays(arr, n, l, r)
    print(v)

# } Driver Code Ends