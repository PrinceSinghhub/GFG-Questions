class Solution:
    def shortestDistance(self, s, word1, word2):
        # code here
        start = 0
        i = 0
        j = 0
        dict_1 = {word1: [], word2: []}
        lst_1 = []
        for i in range(len(s)):
            if s[i] == word1:
                dict_1[word1].append(i)
            elif s[i] == word2:
                dict_1[word2].append(i)

        for i in range(len(dict_1[word1])):
            for k in range(len(dict_1[word2])):
                lst_1.append(abs(dict_1[word1][i] - dict_1[word2][k]))

        return min(lst_1)


# {
#  Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        n = int(input())
        s = list(map(str, input().split()))
        word1 = input()
        word2 = input()
        ob = Solution()
        ans = ob.shortestDistance(s, word1, word2)
        print(ans)