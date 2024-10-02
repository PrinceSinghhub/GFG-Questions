class Solution:
    def countOfSubstrings(self, S, K):
        result = 0
        hash = {}

        for i in range(K):
            hash[S[i]] = hash.get(S[i], 0) + 1
        if len(hash) == K - 1:
            result += 1

        for i in range(K, len(S)):
            hash[S[i]] = hash.get(S[i], 0) + 1

            if hash[S[i - K]] == 1:
                hash.pop(S[i - K])
            else:
                hash[S[i - K]] -= 1

            if len(hash) == K - 1:
                result += 1

        return result