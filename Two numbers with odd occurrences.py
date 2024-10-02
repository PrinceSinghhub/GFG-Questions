from collections import Counter


class Solution:

    def twoOddNum(self, Arr, N):
        dibba = Counter(Arr)

        ans = [i for i in dibba if dibba[i] % 2 != 0]

        return sorted(ans, reverse=True)