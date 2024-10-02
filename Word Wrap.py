import math
class Solution:
    def rec_ww(self, nums, N, K, index, mem):
        if index == N - 1:
            return 0
        if mem[index] != -1:
            return mem[index]
        _sum = 0
        _cost = math.inf
        for i in range(index, N):
            _sum += nums[i]
            if (_sum + i-index) <= K:
                if i == N-1:
                    _cost = 0
                    break
                spaces = K - (_sum + i-index)
                _cost = min(_cost, spaces**2 + self.rec_ww(nums, N, K, i+1, mem))
            else:
                break
        mem[index] = _cost
        return mem[index]

    def solveWordWrap(self, nums, K):
        N =len(nums)
        mem = [-1]*N
        return self.rec_ww(nums, N, K, 0, mem)