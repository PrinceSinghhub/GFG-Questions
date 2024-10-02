class Solution:

    def findMinDiff(self, A,N,M):

       A.sort()
       if M<=N:
          m=10**9
          for i in range(M-1,N):
              if A[i]-A[i-M+1]<m:
                  m=A[i]-A[i-M+1]
          return m

#{
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        N = int(input())
        A = [int(x) for x in input().split()]
        M = int(input())


        solObj = Solution()

        print(solObj.findMinDiff(A,N,M))
# } Driver Code Ends