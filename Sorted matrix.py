class Solution:
    def sortedMatrix(self, N, Mat):

        ans = []

        for i in Mat:
            ans.extend(i)

        ans.sort()

        mymat = []
        index = 0
        for i in range(N):
            temp = []
            for j in range(len(Mat[i])):
                temp.append(ans[index])
                index += 1
            mymat.append(temp)

        return mymat


# {
#  Driver Code Starts
# Initial Template for Python 3

import math

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        v = []
        for i in range(N):
            a = list(map(int, input().strip().split()))
            v.append(a)
        ob = Solution()
        ans = ob.sortedMatrix(N, v)
        for i in range(N):
            for j in range(N):
                print(ans[i][j], end=" ")
            print()