from typing import List


class Solution:
    def getDistinctDifference(self, N: int, A: List[int]) -> List[int]:
        # code here
        arr = [0 for _ in range(N)]
        s = set()
        for i in range(N):
            arr[i] = len(s)
            s.add(A[i])
        s.clear()
        for i in range(N - 1, -1, -1):
            arr[i] -= len(s)
            s.add(A[i])
        return arr


# {
# Driver Code Starts
# class IntArray:

#     def __init__(self) -> None:
#         pass

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        N = int(input())

        A = [int(i) for i in input().split()]

        obj = Solution()
        res = obj.getDistinctDifference(N, A)

        print(*res)

# } Driver Code Ends