class Solution:
    def remove (self, S):
        i = 0
        n = len(S)
        q = []
        while i < n:
            j = i
            while j < n and S[j] == S[i]:
                j += 1
            if j-i == 1:
                q.append(S[i])
            i = j
        s = "".join(q)
        return self.remove(s) if len(s) < len(S) else s


ans = Solution()
print(ans.remove("geeksforgeek"))