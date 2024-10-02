class Solution:
    def Count(self, matrix):
        count=0
        n=len(matrix)
        m=len(matrix[0])
        for i in range(0,n,1):
            for j in range(0,m,1):
                if matrix[i][j]==0:
                    continue
                zero=0
                if i-1>=0:
                    if(matrix[i-1][j])==0:
                        zero+=1
                if i-1>=0 and j+1<m:
                    if(matrix[i-1][j+1]==0):
                        zero+=1
                if j+1<m:
                    if(matrix[i][j+1]==0):
                        zero+=1
                if i+1<n and j+1<m:
                    if(matrix[i+1][j+1]==0):
                        zero+=1
                if i+1<n:
                    if(matrix[i+1][j]==0):
                        zero+=1
                if(i+1<n and j-1>=0):
                    if(matrix[i+1][j-1]==0):
                        zero+=1
                if(j-1>=0):
                    if(matrix[i][j-1]==0):
                        zero+=1
                if(i-1>=0 and j-1>=0):
                    if(matrix[i-1][j-1]==0):
                        zero+=1
                if zero%2==0 and zero!=0:
                    count+=1
        return count


#{
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n, m = input().split()
		n = int(n); m = int(m);
		matrix = []
		for _ in range(n):
			matrix.append(list(map(int,input().split())))
		ob = Solution()
		ans = ob.Count(matrix)
		print(ans)

# } Driver Code Ends