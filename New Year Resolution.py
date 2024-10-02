from typing import List


class Solution:

    def isPossible(self, N, coins):
        return self.HappyNewYear2024(coins, 0, 0)

    def HappyNewYear2024(self, arr, index, sum):
        if index >= len(arr):
            return sum != 0 and (sum == 2024 or sum % 20 == 0 or sum % 24 == 0)

        if sum != 0 and (sum == 2024 or sum % 20 == 0 or sum % 24 == 0):
            return True

        return self.HappyNewYear2024(arr, index + 1, arr[index] + sum) or self.HappyNewYear2024(arr, index + 1, sum)

    # def HappyNewYear2024(self,coins,index,Sum):

    #     if index >= len(coins):
    #         return Sum != 0 and (Sum == 2024 or Sum % 20 == 0 or Sum % 24 == 0)

    #     if(Sum != 0 and (Sum == 2024 or Sum % 20 == 0 or Sum % 24 == 0)):
    #         return True

    #     pick = self.HappyNewYear2024(coins, index+1, coins[index]+Sum)
    #     notPick =self.HappyNewYear2024(arr, index+1, Sum)
    #     return pick or notPick

    # def isPossible(self, N : int, coins : List[int]) -> bool:
    #     return self.HappyNewYear2024(coins,0,0)


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

        coins = IntArray().Input(N)

        obj = Solution()
        res = obj.isPossible(N, coins)

        result_val = 1 if res else 0
        print(result_val)

# } Driver Code Ends