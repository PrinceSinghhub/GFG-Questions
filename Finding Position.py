class Solution:
    def nthPosition(self, n):
        if n == 1:
            return 1

        return self.nthPosition(n // 2) * 2


# {
#  Driver Code Starts
# Initial Template for Python 3
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())

        ob = Solution()
        print(ob.nthPosition(n))