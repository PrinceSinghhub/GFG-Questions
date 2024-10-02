class Solution:
    def UncommonChars(self, A, B):
        A = set(A)
        B = set(B)

        dif1 = list(A.difference(B))
        dif2 = list(B.difference(A))

        dif1.extend(dif2)
        dif1.sort()

        ans = "".join(dif1)

        if len(ans) == 0:
            return -1

        return ans