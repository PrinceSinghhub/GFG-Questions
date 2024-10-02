class Solution:
	def reverseSpiral(self, R, C, matrix):
        out = []
        if R == 0:
            return out
        row_begin = 0
        col_begin = 0
        row_end = R-1 
        col_end = C-1
        while (row_begin <= row_end and col_begin <= col_end):
            for i in range(col_begin,col_end+1):
                out.append(matrix[row_begin][i])
            row_begin += 1
            for i in range(row_begin,row_end+1):
                out.append(matrix[i][col_end])
            col_end -= 1
            if (row_begin <= row_end):
                for i in range(col_end,col_begin-1,-1):
                    out.append(matrix[row_end][i])
                row_end -= 1
            if (col_begin <= col_end):
                for i in range(row_end,row_begin-1,-1):
                    out.append(matrix[i][col_begin])
                col_begin += 1
        return out[::-1]

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        R,C=[int(x) for x in input().split()]
        a=[[0]*C for c in range(R)]
        arr=input().split()
        for i in range(R*C):
            a[i//C][i%C]=int(arr[i])
            
        ob=Solution()
        ans=ob.reverseSpiral(R,C,a)
        for i in range(len(ans)):
            print(ans[i],end=" ")
            
        print()
# } Driver Code Ends


