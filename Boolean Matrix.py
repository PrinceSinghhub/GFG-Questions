def booleanMatrix(matrix):
   # code here
   n=len(matrix)
   m=len(matrix[0])
   a=[0]*n
   b=[0]*m
   for i in range(n):
       for j in range(m):
           if matrix[i][j]==1:
               a[i]=1
               b[j]=1
   for i in range(n):
       for j  in  range(m):
           if (a[i]==1 or b[j]==1):
               matrix[i][j]=1

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
        booleanMatrix(matrix)
        for i in range(r):
            for j in range(c):
                print(matrix[i][j], end=' ')
            print()
