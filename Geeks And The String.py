# User function Template for python3

class Solution:

    def removePair(self, s):
        solution = []
        # Loop once over input appending to solution, unless char matches the
        # last, in which case pop the last and don't append.
        for i in range(len(s)):  # O(N)
            try:
                if solution[-1] == s[i]:  # O(1)
                    solution.pop()  # O(1)
                    continue
            except IndexError:
                pass
            solution.append(s[i])  # O(1)
        return "".join(solution) if solution else "-1"  # O(N)
