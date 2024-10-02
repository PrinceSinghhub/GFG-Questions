class Solution:

    def candyStore(self, candies,N,K):
        # code here
        candies.sort()
        len_ = N
        low = high = 0
        for i in range(len_):
            low = low+candies[i]
            high = high+candies[len_-i-1]
            N-=(1+K)
            if(N<=0):
                break
        return [low,high]


ans = Solution()
n = 4
k = 2
arr = [3,2,1,4]
print(ans.candyStore(arr,n,k))