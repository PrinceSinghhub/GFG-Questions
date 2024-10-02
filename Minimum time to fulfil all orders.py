from typing import List


class Solution:
    def findMinTime(self, n: int, l: int, arr: List[int]) -> int:
        # code here
        ans = []
        for x in arr:
            ele = x
            ans.append(x)
            for i in range(2, n + 1):
                ans.append(ans[-1] + (ele * i))  # keep the count of
                # total time req to bake by one chef
        ans.sort()  # sort
        return ans[n - 1]


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

        l = int(input())

        arr = IntArray().Input(l)

        obj = Solution()
        res = obj.findMinTime(n, l, arr)

        print(res)

# } Driver Code Ends