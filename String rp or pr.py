# User function Template for python3

class Solution:
    def solve(self, X, Y, S):
        # code here
        x = 0
        y = 0
        while ('pr' in S or 'rp' in S):
            if X >= Y:
                while ('pr' in S):
                    x += S.count('pr')
                    S = S.replace('pr', '')
                while ('rp' in S):
                    y += S.count('rp')
                    S = S.replace('rp', '')
            else:
                while ('rp' in S):
                    y += S.count('rp')
                    S = S.replace('rp', '')
                while ('pr' in S):
                    x += S.count('pr')
                    S = S.replace('pr', '')
        return X * x + Y * y


# {
# Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        str = input().split()
        X = int(str[0])
        Y = int(str[1])
        S = input()

        ob = Solution()
        print(ob.solve(X, Y, S))
# } Driver Code Ends