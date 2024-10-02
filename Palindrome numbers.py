class Solution:
    def isPallindrome(self, N):
        Con = bin(N)[2::]

        if Con == Con[::-1]:
            return 1
        return 0


# {
#  Driver Code Starts
# Initial Template for Python 3


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        print(ob.isPallindrome(N))