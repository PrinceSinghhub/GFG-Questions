# User function Template for python3

class Solution:
    def columnWithMaxZeros(self, arr, N):
        # code here
        Maxres = 0
        col = -1
        r = c = N

        for j in range(c):
            res = 0
            for i in range(r):
                if arr[i][j] == 0:
                    res += 1
            if res > Maxres:
                Maxres = res
                col = j

        return col


# {
# Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        arr = []
        for i in range(N):
            line = [int(x) for x in input().strip().split()]
            arr.append(line)
        ob = Solution()
        print(ob.columnWithMaxZeros(arr, N))

# } Driver Code Ends