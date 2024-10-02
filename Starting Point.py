class Solution:

    def findStartingPoint(self, x, y, pathCoordinates):
        summ=0
        result_list=[]
        n =len(pathCoordinates)
        for j in range(0,2):
             for i in range(0,n):
                 summ += pathCoordinates[i][j]
             if j==0:
                 result_list.append(x-summ)
             if j==1:
                 result_list.append(y-summ)
             summ=0
        return result_list