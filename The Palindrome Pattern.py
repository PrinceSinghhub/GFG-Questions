# User function Template for python3

class Solution:
    def pattern(self, arr):

        # code here
        rows = []
        m = len(arr)
        for i in range(0, m):
            rows.append("".join([str(val) for val in arr[i]]))
        # Rows
        for i in range(0, m):
            if rows[i] == rows[i][::-1]:
                return "{} R".format(i)
        for i in range(0, m):
            j, k = 0, m - 1
            while j < k:
                if rows[j][i] != rows[k][i]:
                    break
                j += 1
                k -= 1
            if j >= k:
                return "{} C".format(i)
        return "-1"


# {
# Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    ob = Solution()
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        a = list()
        c = 0
        for i in range(0, n):
            X = list()
            for j in range(0, n):
                X.append(arr[c])
                c += 1
            a.append(X)
        ans = ob.pattern(a)
        print(ans)

# } Driver Code Ends