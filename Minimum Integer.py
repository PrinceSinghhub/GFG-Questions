from typing import List


class Solution:
    def minimumInteger(self, N: int, A: List[int]) -> int:
        # code here
        s = sum(A)
        res = 0
        for i in A:
            if (i * N >= s):
                if (res == 0):
                    res = i
                else:
                    res = min(res, i)
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
        N = int(input())

        A = IntArray().Input(N)

        obj = Solution()
        res = obj.minimumInteger(N, A)

        print(res)

# } Driver Code Ends