class Solution:
    def inSequence(self, A, B, C):
        if C == 0: return 1 if A == B else 0
        n = (B + C - A) / C
        return 1 if n * 10 == int(n) * 10 and n > 0 else 0


# {
# Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        A, B, C = [int(x) for x in input().split()]

        ob = Solution();
        print(ob.inSequence(A, B, C))
# } Driver Code Ends