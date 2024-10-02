# User function Template for Python3

class Solution:
    @staticmethod
    def maxGold(n, m, a):
        row = len(a)
        col = len(a[0])
        dp = [[0] * col for _ in range(row)]
        max_gold = 0

        if row == 1:
            max_gold = sum(a[0])
        else:
            for j in range(col - 2, -1, -1):
                for i in range(row):
                    if i == 0:
                        a[i][j] += max(a[i][j + 1], a[i + 1][j + 1])
                    elif i == row - 1:
                        a[i][j] += max(a[i][j + 1], a[i - 1][j + 1])
                    else:
                        a[i][j] += max(a[i][j + 1], max(a[i - 1][j + 1], a[i + 1][j + 1]))

            max_gold = max(a[i][0] for i in range(row))

        return max_gold


# {
# Driver Code Starts
# Initial Template for Python3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, m = [int(x) for x in input().split()]
        tarr = [int(x) for x in input().split()]
        M = []
        j = 0
        for i in range(n):
            M.append(tarr[j:j + m])
            j = j + m

        ob = Solution()
        print(ob.maxGold(n, m, M))
# } Driver Code Ends