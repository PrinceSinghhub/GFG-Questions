# {
# Driver Code Starts
# Initial Template for Python 3

import atexit
import io
import sys


# } Driver Code Ends
# User function Template for python3

class Solution:

    def combinationalSum(self, A, B):
        def combinationSum(A, B, i, sum_arr, result):
            if B == 0:
                sum_arr.sort()
                result.append(sum_arr)
                return

            for j in range(i, len(A)):
                if A[j] > 0:
                    if j > i and A[j] == A[j - 1]: continue
                    if A[j] > B: break
                    combinationSum(A, (B - A[j]), j, sum_arr + [A[j]], result)

        result = []
        combinationSum(sorted(A), B, 0, [], result)
        result.sort()
        return result

    # def findAllcombinationSum(self, index, candidates, target, ans, ds):

    #     if index == len(candidates):
    #         if target == 0:
    #             ds.sort()
    #             if ds not in ans:
    #                 ans.append(ds[:])
    #                 return
    #             return
    #         return

    #     if candidates[index] <= target:
    #         ds.append(candidates[index])
    #         self.findAllcombinationSum(index, candidates, target - candidates[index], ans, ds)
    #         ds.remove(candidates[index])

    #     self.findAllcombinationSum(index + 1, candidates, target, ans, ds)

    # def combinationalSum(self,A, B):

    #     ans = []
    #     self.findAllcombinationSum(0,A,B,ans,[])

    #     ans.sort()
    #     return ans

    # code here


# {
# Driver Code Starts.


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        a = list(map(int, input().strip().split()))
        s = int(input())
        ob = Solution()
        result = ob.combinationalSum(a, s)
        if (not len(result)):
            print("Empty")
            continue
        for i in range(len(result)):
            print("(", end="")
            size = len(result[i])
            for j in range(size - 1):
                print(result[i][j], end=" ")
            if (size):
                print(result[i][size - 1], end=")")
            else:
                print(")", end="")
        print()

# } Driver Code Ends