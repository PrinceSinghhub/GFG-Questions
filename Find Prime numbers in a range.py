class Solution:
    def checkprime(self, num):
        if num == 1:
            return False

        for i in range(2, num):
            if num % i == 0:
                return False

        return True

    def primeRange(self, M, N):

        ans = []

        for i in range(M, N):
            check = self.checkprime(i)
            if check == True:
                ans.append(i)

        return ans


# {
#  Driver Code Starts
# Initial Template for Python 3

import math

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        M, N = map(int, input().strip().split(" "))
        ob = Solution()
        ans = ob.primeRange(M, N)
        for i in ans:
            print(i, end=" ")
        print()
        # } Driver Code Ends