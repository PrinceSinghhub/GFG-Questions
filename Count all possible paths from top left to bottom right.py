# User function Template for python3

# code studio Problem : Total Unique Paths

class Solution1:

    def SpaceOptimization_Methode(self, row, coll):

        dp = [-1] * coll

        for i in range(row):

            dummy = [-1] * coll

            for j in range(coll):

                if i == 0 and j == 0:
                    dummy[j] = 1
                    continue

                up = 0
                left = 0

                if i > 0:
                    up = dp[j]

                if j > 0:
                    left = dummy[j - 1]

                dummy[j] = up + left

            dp = dummy

        # print(dp)
        return dp[coll - 1]

    def TotalUniquePath(self, row, collom):

        ans = self.SpaceOptimization_Methode(row, collom)
        return ans


class Solution:
    def numberOfPaths(self, m, n):
        ans = Solution1()
        return ans.TotalUniquePath(m, n) % 1000000007


# {
#  Driver Code Starts
# Initial Template for Python 3
if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        m, n = input().split()
        m = int(m)
        n = int(n)
        ob = Solution();
        print(ob.numberOfPaths(m, n))

# } Driver Code Ends