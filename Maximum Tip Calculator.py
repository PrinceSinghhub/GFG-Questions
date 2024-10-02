from typing import List

from typing import List


class Solution:
    def maxTip(self, n: int, x: int, y: int, arr: List[int], brr: List[int]) -> int:
        # code here
        res = 0
        chq = {}
        tst = []
        for i in range(n):
            chq[i] = max(arr[i] - brr[i], brr[i] - arr[i])
            tst.append((max(arr[i] - brr[i], brr[i] - arr[i]), i))

        a_chq = 0
        b_chq = 0
        te = sorted(tst, reverse=True)
        # print(te)
        # te = sorted(chq.items(),reverse=True)
        # pe = sorted(chq.values(),reverse=True)
        # print(pe)
        for i in te:
            if a_chq >= x:
                res += brr[i[1]]
            elif b_chq >= y:
                res += arr[i[1]]
            elif arr[i[1]] >= brr[i[1]]:
                res += arr[i[1]]
                a_chq += 1
            elif arr[i[1]] <= brr[i[1]]:
                res += brr[i[1]]
                b_chq += 1
        return res


# {
# Driver Code Starts
class IntArray:

    def __init__(self) -> None:
        pass

    def Input(self, n):
        arr = [int(i) for i in input().strip().split()]  # array input
        return arr

    def Print(self, arr):
        for i in arr:
            print(i, end=" ")
        print()


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())

        x = int(input())

        y = int(input())

        arr = IntArray().Input(n)

        brr = IntArray().Input(n)

        obj = Solution()
        res = obj.maxTip(n, x, y, arr, brr)

        print(res)

# } Driver Code Ends