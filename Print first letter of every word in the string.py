class Solution:
    def firstAlphabet(self, S):
        S1=S.strip()
        res = ''
        res += S1[0]
        for i in range(len(S1)):

            if S1[i] == " ":
                res+=S1[i+1]
        # res.strip()
        # print(S1)
        return res





# code here

# {
#  Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        S = input()
        ob = Solution()
        answer = ob.firstAlphabet(S)

        print(answer)