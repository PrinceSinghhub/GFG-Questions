class Solution:
    def pattern(self, n):
        # code here
        total = int(((n * (n + 1)) / 2) * 2)
        interval = 0
        result = []
        for i in range(n, 0, -1):
            subStr = ""
            subStr += "-" * (n - i) * 2
            for j in range(interval + 1, interval + i + 1):
                subStr += str(j)
                subStr += "*"
            for k in range(total - i - interval + 1, total - interval + 1):
                subStr += str(k)
                if total - interval != k:
                    subStr += "*"
            interval += i
            result.append(subStr)
        return result


# {
# Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())

        ob = Solution()
        ans = ob.pattern(n)
        for i in range(n):
            print(ans[i])
# } Driver Code Ends