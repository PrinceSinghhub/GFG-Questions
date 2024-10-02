from functools import lru_cache


class Solution:

    @lru_cache(None)
    def isScramble(self, S1: str, S2: str):
        ##code here
        if S1 == S2: return True
        if sorted(S1) != sorted(S2): return False

        for i in range(1, len(S1)):
            if (self.isScramble(S1[:i], S2[:i]) and self.isScramble(S1[i:], S2[i:])) or (
                    self.isScramble(S1[:i], S2[-i:]) and self.isScramble(S1[i:], S2[:-i])):
                return True
        return False


# {
# Driver Code Starts
# Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        S1, S2 = input().split()
        if (Solution().isScramble(S1, S2)):
            print("Yes")

        else:
            print("No")

# } Driver Code Ends