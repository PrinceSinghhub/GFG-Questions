class Solution:
    def endPoints(self, matrix, m, n):
        def get(x,y,d):
            if d=='R':
                return (x,y+1)
            elif d=='L':
                return (x,y-1)
            elif d=='U':
                return (x-1,y)
            else:
                return (x+1,y)
        def solve(x,y,d):
            if matrix[x][y] == 0:
                nx,ny = get(x,y,d)
                nd = d
            else:
                matrix[x][y] = 0
                if d=='U':
                    nx,ny = get(x,y,'R')
                    nd = 'R'
                elif d=='R':
                    nx,ny = get(x,y,'D')
                    nd = 'D'
                elif d=='D':
                    nx,ny = get(x,y,'L')
                    nd = 'L'
                elif d=='L':
                    nx,ny = get(x,y,'U')
                    nd = 'U'
            #print(nx,ny,nd)
            if 0<=nx<len(matrix) and 0<=ny<len(matrix[0]):
                return solve(nx,ny,nd)
            else:
                return (x,y)
        return solve(0,0,'R')

#{
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        r,c = map(int, input().strip().split())
        matrix = []
        for i in range(r):
            line = [int(x) for x in input().strip().split()]
            matrix.append(line)
        ob = Solution()
        ans = ob.endPoints(matrix,r,c)
        print('(',ans[0],', ',ans[1],')',sep ='')