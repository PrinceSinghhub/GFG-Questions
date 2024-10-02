from collections import Counter
class Solution:
    def transform(self, A, B):
        #failure cases
        if len(A) != len(B):
            return -1
        #failure cases
        resA = Counter(A)
        resB = Counter(B)
        if resA != resB:
            return -1
        #ans case
        #trverse kar rha hu dono string me form back
        #and if char in both string matches i-1 j -1
        #since me sif string A me hi change kar saktha hu
        #toh agar match nhi kar rha toh string A me decrease karuga
        ans = 0
        i = len(A)-1
        j = len(B)-1
        while i >= 0 and j >= 0:
            if A[i] == B[j]:
                i -= 1
                j -= 1
            else:
                i -= 1
                ans += 1
        return ans