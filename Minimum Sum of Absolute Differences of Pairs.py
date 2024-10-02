class Solution:
    def findMinSum(self, A, B, N):
        return sum([abs(x-y) for (x, y) in zip(sorted(A), sorted(B))])


#{
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        A = list(map(int, input().strip().split()))
        B = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.findMinSum(A,B,N)
        print(ans)
# } Driver Code Ends