# User function Template for python3

class Solution:
    def shortestPath(self, x, y):
        if x == y:
            return 0

        Max = max(x, y)
        Min = min(x, y)

        return 1 + self.shortestPath(Max // 2, Min)


# {
#  Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        x, y = map(int, input().strip().split())
        ob = Solution()
        print(ob.shortestPath(x, y))
# } Driver Code Ends