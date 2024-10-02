class Solution:
    def countZeroes(self, matrix, n):
        l=len(matrix)
        r=[]
        result = 0
        for i in range(l):
            t=matrix[i]
            t.sort()
            r.append(t)
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] ==0:
                    result+=1
        return result





# {
#  Driver Code Starts
# Your code goes here
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input("ITERATION").strip())
        arr = list(map(int, input("Enter").strip().split()))
        matrix = [[0 for i in range(n)] for j in range(n)]
        k = 0
        for i in range(n):
            for j in range(n):
                matrix[i][j] = arr[k]
                k += 1

        ob = Solution()
        print(ob.countZeroes(matrix, n))
