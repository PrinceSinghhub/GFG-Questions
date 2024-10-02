#User function Template for python3

# User function Template for python3
from collections import Counter


class Solution:
    def winner(self, arr, n):
        data = dict(Counter(arr))
        winner = max(data.values())
        for ele in sorted(data.keys()):
            if data[ele] == winner:
                return [ele , winner]