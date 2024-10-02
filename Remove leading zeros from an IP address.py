class Solution:
    def newIPAdd(self, S):
        arr = S.split('.')

        arr = list(map(int, arr))

        for i in arr:
            x = i * 1

        arr = list(map(str, arr))

        S = ".".join(arr)

        return S


# {
#  Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input().strip()
        ob = Solution()
        ans = ob.newIPAdd(s)
        print(ans)
# } Driver Code Ends