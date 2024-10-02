import numpy as np


class Solution:
    def polyMultiply(self, Arr1, Arr2, M, N):
        a = np.array(Arr1)
        b = np.array(Arr2)
        return np.polymul(a, b)


# {
# Driver Code Starts
# Initial Template for Python 3

# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        M, N = input().split()
        M = int(M)
        N = int(N)
        Arr1 = input().split()
        for itr in range(M):
            Arr1[itr] = int(Arr1[itr])

        Arr2 = input().split()
        for itr in range(N):
            Arr2[itr] = int(Arr2[itr])

        ob = Solution()
        ans = ob.polyMultiply(Arr1, Arr2, M, N)
        for i in range(len(ans)):
            print(ans[i], end=" ")
        print()
# } Driver Code Ends