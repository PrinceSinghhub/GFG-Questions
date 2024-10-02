import bisect as bt


class Solution:
    def countEleLessThanOrEqual(self, arr1, n1, arr2, n2):
        arr2.sort()
        res = []
        for e in arr1:
            res.append(bt.bisect(arr2, e))

        return res


# {
#  Driver Code Starts
# Initial Template for Python 3

# contributed by RavinderSinghPB
if __name__ == '__main__':
    t = int(input())

    for tcs in range(t):

        n1, n2 = [int(x) for x in input().split()]
        arr1 = [int(x) for x in input().split()]
        arr2 = [int(x) for x in input().split()]

        res = Solution().countEleLessThanOrEqual(arr1, n1, arr2, n2)
        for i in range(len(res)):
            print(res[i], end=" ")
        print()