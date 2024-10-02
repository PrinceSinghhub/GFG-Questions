class Solution:
    def minRow(self, A):

        ans = [i.count(1) for i in A]
        ans.sort()
        ans1 = 999999999999999

        for j in range(len(A)):
            if min(ans) == A[j].count(1) and j < ans1:
                ans1 = j + 1

        return ans1

ans = Solution()
A=[[1,1,1,1],[1,1,0,0],[0,0,1,1],[1,1,1,1]]
print(ans.minRow(A))