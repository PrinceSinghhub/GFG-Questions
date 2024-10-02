from typing import List


class Solution:
    def getMinimumDays(self, N: int, S: str, P: List[int]) -> int:
        # code here
        c = 0
        l = list(S)
        for i in range(N - 1):
            while l[i] == l[i + 1] and l[i] != '?':
                l[P[c]] = '?'
                c += 1
        return c


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
        N = int(input())

        S = (input())

        P = IntArray().Input(N)

        obj = Solution()
        res = obj.getMinimumDays(N, S, P)

        print(res)

# } Driver Code Ends