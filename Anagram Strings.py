# User function Template for python3
class Solution:
    def areAnagram(ob, S1, S2):

        if len(S1) != len(S2):
            return 0

        S1 = sorted(S1)
        S2 = sorted(S2)

        if "".join(S1) == "".join(S2):
            return 1

        return 0