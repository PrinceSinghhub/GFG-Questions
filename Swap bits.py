class Solution:

   def swapBits(self, X, p1, p2, N):

       for i in range(N):

           temp = (X>>(i+p1) & 1)^(X>>(i+p2) & 1)

           X^=(temp<<(i+p1))

           X^=(temp<<(i+p2))

       return X



#{
#  Driver Code Starts

if __name__ == '__main__':
    t = int (input ())
    for _ in range (t):
        obj = Solution()
        X, P1, P2, N = map(int, input().split())
        print(obj.swapBits(X, P1, P2, N))