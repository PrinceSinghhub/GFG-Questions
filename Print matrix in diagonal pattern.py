# Your task is to complete this function

class Solution:
    def matrixDiagonally(self,mat):
        i,j=0,0
        res=[mat[i][j]]
        r=len(mat)
        c=len(mat[0])
        while i<r-1 or j<c-1:
            if j+1 <c:
                j+=1
                res.append(mat[i][j])
            else:
                i+=1
                res.append(mat[i][j])
            while i+1<r and j-1 >=0:
                i+=1
                j-=1
                res.append(mat[i][j])
            if i+1<r:
                i+=1
                res.append(mat[i][j])
            else:
                j+=1
                res.append(mat[i][j])
            while i-1>=0 and j+1<c:
                i-=1
                j+=1
                res.append(mat[i][j])
        return res

#{
 # Driver Code Starts
# Driver Program
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        matrix = [[0 for i in range(n[0])]for j in range(n[0])]
        k=0
        for i in range(n[0]):
            for j in range(n[0]):
                matrix[i][j] = arr[k]
                k+=1
        a = Solution().matrixDiagonally(matrix)
        for x in a:
            print(x,end=' ')
        print('')
# Contributed by: Harshit Sidhwa
# } Driver Code Ends