class Solution:
    def maxOnes(self, Mat, N, M):

        count = -999999999
        index = 0
        for i in range(len(Mat)):

            if Mat[i].count(1) > count:
                count = Mat[i].count(1)
                index = i

        return index


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        size = input().strip().split()
        r = int(size[0])
        c = int(size[1])
        line = list(map(int,input().split()))
        matrix = [ [0 for _ in range(c)] for _ in range(r) ]
        for i in range(r):
            for j in range(c):
                matrix[i][j] = line[i*c+j]
                ob = Solution()
            print(ob.maxOnes(matrix,r,c))