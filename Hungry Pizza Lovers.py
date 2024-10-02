class Solution:
    def permute(self, arr, n):
        ans = [ans[1] for ans in sorted((arr[i][0] + arr[i][1], i + 1) for i in range(n))]
        return ans
        # Complete the function


# {
#  Driver Code Starts
# Initial Template for Python 3


for _ in range(0, int(input())):
    n = int(input())
    arr = []
    for _ in range(0, n):
        ll = list(map(int, input().strip().split()))
        arr.append(ll)
    obj = Solution()
    ans = obj.permute(arr, n)
    for i in ans:
        print(i)

# } Driver Code Ends