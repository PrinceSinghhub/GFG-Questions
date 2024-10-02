class Solution:

    def canMakeTriangle(self, A, N):
        ans = []
        for i in range(N - 2):
            a, b, c = A[i:i + 3]
            if a + b <= c or a + c <= b or b + c <= a:
                ans.append(0)
            elif (a + b > c and a + c > b and b + c > a):
                ans.append(1)
        return ans


# {
#  Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        A = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.canMakeTriangle(A, N)
        for i in ans:
            print(i, end=" ")
        print()

# } Driver Code Ends