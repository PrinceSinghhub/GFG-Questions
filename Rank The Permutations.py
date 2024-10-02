class Solution:

    def factorial(self, n):
        fact = 1
        for i in range(1, n + 1):
            fact = fact * i
        return fact

    def findRank(self, S):
        # Code here
        rank = 1
        for i in range(len(S) - 1):
            count = 0
            for j in range(i + 1, len(S)):
                if S[i] > S[j]:
                    count += 1
            rank += count * self.factorial(len(S) - 1 - i)

        return rank


if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        str = input().strip()
        obj = Solution()
        ans = obj.findRank(str)
        print(ans)