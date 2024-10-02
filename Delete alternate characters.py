class Solution:
    def delAlternate(ob, S):
        output = ""
        for i in range(len(S)):
            if i%2==0:
                output+=S[i]
        return output

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        S = input()
        ob = Solution()
        print(ob.delAlternate(S))