from typing import List


class Solution:
    def totalTime(self, n: int, arr: List[int], time: List[int]) -> int:
        # code here
        myset = set()
        ans = 0
        for i in range(0, n):
            if arr[i] in myset:
                ans += time[arr[i] - 1]
            else:
                myset.add(arr[i])
                ans += 1
        return ans - 1


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

        arr = IntArray().Input(n)

        time = IntArray().Input(n)

        obj = Solution()
        res = obj.totalTime(n, arr, time)

        print(res)

# } Driver Code Ends