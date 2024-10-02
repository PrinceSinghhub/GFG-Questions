class Solution:
    def kadanesAlgo(self, submat, c):

        a = submat[0]
        Max = submat[0]

        for i in range(1, c):
            a += submat[i]
            a = max(a, submat[i])
            Max = max(a, Max)

        return Max

    def maximumSumRectangle(self, R, C, M):
        res = M[0][0]
        for i in range(R):
            subMatSum = [0 for _ in range(C)]
            for i in range(i, R):
                for j in range(C):
                    subMatSum[j] += M[i][j]
                res = max(res, self.kadanesAlgo(subMatSum, C))
        return res

ans = Solution()
R=4
C=5
M=[[1,2,-1,-4,-20],
[-8,-3,4,2,1],
[3,8,10,1,3],
[-4,-1,1,7,-6]]
print(ans.maximumSumRectangle(R,C,M))