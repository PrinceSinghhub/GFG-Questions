from typing import List

from typing import List


class Solution:

    def largestArea(self, n: int, m: int, k: int, enemy: List[List[int]]) -> int:

        # code here

        tot = n * m

        if k == 0: return tot

        row = []

        col = []

        road = []

        coad = []

        for i, j in enemy:
            row.append(i)

            col.append(j)

        row = sorted(row)

        col = sorted(col)

        row.insert(0, 0)

        col.insert(0, 0)

        if (row[-1] == n):

            row.append((row[-1] + 1))

        else:

            row.append(n + 1)

        if (col[-1] == m):

            col.append((col[-1] + 1))

        else:

            col.append(m + 1)

        for k in range(len(row) - 1):
            road.append((row[k + 1] - row[k] - 1))

        for l in range(len(col) - 1):
            coad.append((col[l + 1] - col[l] - 1))

        return (max(road) * max(coad))


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
        a = IntArray().Input(3)
        n, m, k = a[0], a[1], a[2]

        e = IntMatrix().Input(a[2], 2)

        obj = Solution()
        res = obj.largestArea(n, m, k, e)

        print(res)

# } Driver Code Ends