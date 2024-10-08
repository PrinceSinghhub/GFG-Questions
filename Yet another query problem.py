from typing import List


class Solution:
    def solveQueries(self, N: int, num: int, A: List[int], Q: List[List[int]]) -> List[int]:
        suffixocc = [0] * N
        suffixmap = dict()
        for i in range(N - 1, -1, -1):
            if A[i] not in suffixmap:
                suffixmap[A[i]] = 1
            else:
                suffixmap[A[i]] += 1
            suffixocc[i] = suffixmap[A[i]]

        arr = [suffixocc[l:r + 1].count(k) for l, r, k in Q]
        return arr


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


class IntMatrix:
    def __init__(self) -> None:
        pass

    def Input(self, n, m):
        matrix = []
        # matrix input
        for _ in range(n):
            matrix.append([int(i) for i in input().strip().split()])
        return matrix

    def Print(self, arr):
        for i in arr:
            for j in i:
                print(j, end=" ")
            print()


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        N = int(input())

        num = int(input())

        A = IntArray().Input(N)

        Q = IntMatrix().Input(num, 3)

        obj = Solution()
        res = obj.solveQueries(N, num, A, Q)

        IntArray().Print(res)

# } Driver Code Ends