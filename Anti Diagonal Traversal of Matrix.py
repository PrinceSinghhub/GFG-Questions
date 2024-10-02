#User function Template for python3
from collections import deque


class Solution:
    def antiDiagonalPattern(self,matrix):
        # Code here
        n,m = len(matrix), len(matrix[0])
        q = deque()
        q.append((0,0))
        vis = [[False for _ in range(n)] for _ in range(m)]
        vis[0][0] = True
        res = []
        directions = [[0,1],[1,0]]
        while q:
            l = len(q)
            for _ in range(l):
                i,j = q.popleft()
                res.append(matrix[i][j])
                for r,c in directions:
                    new_i = i+r
                    new_j = j+c
                    if new_i>=0 and new_i<n and new_j>=0 and new_j<m and not vis[new_i][new_j]:
                        q.append((new_i,new_j))
                        vis[new_i][new_j] = True
        return res


#{
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        inp=list(map(int,input().split()))
        matrix=[]
        k = 0
        for i in range(n):
            row = []
            for j in range(n):
                row.append(inp[k])
                k += 1
            matrix.append(row)
        ob = Solution()
        ans = ob.antiDiagonalPattern(matrix)
        for i in ans:
            print(i,end=" ")
        print()


# } Driver Code Ends