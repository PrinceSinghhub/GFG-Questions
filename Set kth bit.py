class Solution:
    def setKthBit(self, N, K):
        return N | 1 << K