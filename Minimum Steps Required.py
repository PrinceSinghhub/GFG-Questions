class Solution:
    def minSteps(self, s) -> int:
        a = 0
        b = 0
        i = 0

        while i < len(s):
            if s[i] == "a":
                a += 1
                while i < len(s) and s[i] == "a":
                    i += 1
            else:
                b += 1
                while i < len(s) and s[i] == "b":
                    i += 1
        return min(a, b) + 1

    