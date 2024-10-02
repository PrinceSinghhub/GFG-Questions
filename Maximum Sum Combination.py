class Solution:
    def maxCombinations(self, N, K, A, B):
        A.sort()
        B.sort()
        ans=[]
        mxh=[]
        import heapq as hq
        for idx in range(N):
            hq.heappush(mxh,(-A[N-1]-B[idx],N-1,idx,))
        for cnt in range(K):
            tmp=hq.heappop(mxh)
            ans.append(-tmp[0])
            hq.heappush(mxh,(-A[tmp[1]-1]-B[tmp[2]],tmp[1]-1,tmp[2],))
        return ans