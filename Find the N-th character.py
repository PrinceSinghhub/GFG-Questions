# User function Template for python3

class Solution:
    def nthCharacter(self, s, r, n):
        corr = {
            '1': '10',
            '0': '01'
        }

        r = 1 << r

        while r > 1:
            index = n // r
            s = corr[s[index]]
            if n >= r:
                n = n % r
            r = r // 2

        return s[n // r]


# {
# Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        snr = input().split()
        S, R, N = snr[0], int(snr[1]), int(snr[2])
        ob = Solution()
        print(ob.nthCharacter(S, R, N))
# } Driver Code Ends