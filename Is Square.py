# User function Template for python3

class Solution:
    def isSquare(self, x1, y1, x2, y2, x3, y3, x4, y4):
        return 'Yes' if len(set([x1, y1, x2, y2, x3, y3, x4, y4])) == 2 else 'No';


# {
# Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        x1, y1, x2, y2, x3, y3, x4, y4 = map(int, input().split())

        ob = Solution()
        print(ob.isSquare(x1, y1, x2, y2, x3, y3, x4, y4))
# } Driver Code Ends