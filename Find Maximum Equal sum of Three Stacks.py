from typing import List


class Solution:
    def maxEqualSum(self, N1: int, N2: int, N3: int, S1: List[int], S2: List[int], S3: List[int]) -> int:
        sum1, sum2, sum3 = sum(S1), sum(S2), sum(S3)
        top1, top2, top3 = 0, 0, 0

        while True:
            if top1 == N1 or top2 == N2 or top3 == N3:
                return 0

            if sum1 == sum2 == sum3:
                return sum1

            if sum1 >= sum2 and sum1 >= sum3:
                sum1 -= S1[top1]
                top1 += 1

            elif sum2 >= sum1 and sum2 >= sum3:
                sum2 -= S2[top2]
                top2 += 1

            else:
                sum3 -= S3[top3]
                top3 += 1

        return sum1


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
        a = IntArray().Input(3)

        S1 = IntArray().Input(a[0])

        S2 = IntArray().Input(a[1])

        S3 = IntArray().Input(a[2])

        obj = Solution()
        res = obj.maxEqualSum(a[0], a[1], a[2], S1, S2, S3)

        print(res)

# } Driver Code Ends