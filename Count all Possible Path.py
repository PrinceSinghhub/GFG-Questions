class Solution:
    def isPossible(self, paths):
        for val in paths:
            if val.count(1) % 2:
                return 0

        return 1