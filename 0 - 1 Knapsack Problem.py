from numpy import *


class Solution:
    def knapSack(self, W, wt, val, n):
        items = n
        weight = wt
        profit = val

        arr = ones((items+1,W+1),int)
        for i in range(len(arr)):
            for j in range(len(arr[i])):
                arr[0][j] = 0
                arr[i][0] = 0

        for i in range(1,len(arr)):
            for j in range(1,len(arr[i])):
                if weight[i-1] <=j:
                    arr[i][j] = max(profit[i-1]+arr[i-1][j-weight[i-1]],arr[i-1][j])

                else:
                    arr[i][j] = arr[i-1][j]
        return arr[len(arr)-1][W]

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        W = int(input())
        val = list(map(int, input().strip().split()))
        wt = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.knapSack(W, wt, val, n))