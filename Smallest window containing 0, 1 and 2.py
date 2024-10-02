class Solution:
    def smallestSubstring(self, S):
        zero = -1
        one = -1
        two = -1

        ans = float('inf')

        for i in range(len(S)):
            if S[i] == '0':
                zero = i
            elif S[i] == '1':
                one = i
            else:
                two = i

            if zero != -1 and one != -1 and two != -1:
                maximum = max(zero, max(one, two))
                minimum = min(zero, min(one, two))
                ans = min(ans, maximum - minimum + 1)

        return -1 if ans == float('inf') else ans