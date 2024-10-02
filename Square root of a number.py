class Solution:
    def floorSqrt(self, x):
        return int(math.sqrt(x))



import math


def main():
    T = int(input())
    while (T > 0):
        x = int(input())

        print(Solution().floorSqrt(x))

        T -= 1
