class Solution:

    def isPossible(self, S):

        S = S.lower()
        count = []
        s = set(S.lower())
        # print(s)
        for i in s:
            count.append(S.count(i))

        # print(count)
        odd = 0
        for i in count:
            if i & 1:
                odd += 1
            if odd > 1:
                return False
        return True 