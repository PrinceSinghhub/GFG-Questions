class Solution:
    def numIslands(self,grid):
        #code here
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    #print(i,j,grid)
                    grid[i][j] = 0
                    self.helper(grid,i,j)
                    count += 1
        return count
    # use a helper function to flip connected '1's to 0
    def helper(self,grid,i,j):
        queue = deque([(i,j)])
        while queue:
            I,J = queue.popleft()
            for i,j in [I+1,J],[I,J+1],[I-1,J],[I,J-1],[I+1,J+1,],[I-1,J-1],[I+1,J-1],[I-1,J+1]:
                if  i  in range(len(grid)) and  j in range(len(grid[0])) and grid[i][j] == 1:
                    #print(i,j, queue)
                    grid[i][j] = 0
                    queue.append((i,j))

#{
#  Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    for _ in range(int(input())):
        n,m=map(int,input().strip().split())
        grid=[]
        for i in range(n):
            grid.append([int(i) for i in input().strip().split()])
        obj=Solution()
        print(obj.numIslands(grid))
# } Driver Code Ends