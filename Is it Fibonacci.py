# User function Template for python3

class Solution():
    def solve(self, n, k, arr):
        su, m, i = sum(arr), n - k - 1, 0
        if m < 0:
            return arr[n - 1]
        arr.append(su)
        for i in range(m):
            su += arr[-1] - arr[i]
            arr.append(su)
        return arr[-1]


# {
# Driver Code Starts
# Initial Template for Python 3

if __name__ == "__main__":
    for _ in range(int(input())):
        N, K = map(int, input().split())
        GeekNum = [int(i) for i in input().split()]
        print(Solution().solve(N, K, GeekNum))

# } Driver Code Ends