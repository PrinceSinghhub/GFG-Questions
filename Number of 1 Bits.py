class Solution:
    def setBits(self, N):
        ans = str(bin(N))
        ans = ans[2::]

        return ans.count('1')


# {
#  Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        N = int(input())
        ob = Solution()
        ans = ob.setBits(N)
        print(ans)
