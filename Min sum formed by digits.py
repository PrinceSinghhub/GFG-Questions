class Solution:
    def minSum(self, arr, n):
        # Your code goes here
        if(n <=2):
            return sum(arr)
        arr.sort()
        res1 = 0
        res2 = 0
        # print(arr)
        for i in range(0,n,2):
            res1=(10*res1+arr[i])
            try:
                res2 = (10*res2+arr[i+1])
            except:
                pass
        return (res1+res2)