# You are required to complete this method
# Return True/False or 1/0
def isToeplitz(mat):
    c=0
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if i<len(mat)-1 and j<len(mat[0])-1:
                if mat[i][j]!=mat[i+1][j+1]:
                    c=1
                    break
    if c!=1:
        return True
    else:
        return False


#{
 # Driver Code Starts
# Your code goes here
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n, m = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        matrix = [[0 for i in range(m)] for j in range(n)]
        k = 0
        for i in range(n):
            for j in range(m):
                matrix[i][j] = arr[k]
                k += 1
        b = isToeplitz(matrix)

        if b == True:
            print("true")
        else:
            print("false")

# } Driver Code Ends