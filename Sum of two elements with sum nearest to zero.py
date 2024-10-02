class Solution:
    def closestToZero(self, arr, n):

        arr.sort()
        minSum=1000000
        i=0
        j=len(arr)-1
        temp=0
        while(j>0 and i<len(arr)-1):
            if(arr[i]+arr[j]<0):
                if(abs(minSum)>=abs(arr[i]+arr[j])):
                    temp=minSum
                    minSum=arr[i]+arr[j]
                    if(temp==1 and arr[i]+arr[j]==-1):
                        minSum=1
                i+=1
            elif(arr[i]+arr[j]>0):
                if(abs(minSum)>=abs(arr[i]+arr[j])):
                    if(minSum!=1):
                        minSum=(arr[i]+arr[j])
                j-=1
            elif(arr[i]+arr[j]==0):
                return 0
        return minSum

#{ 
#  Driver Code Starts
#Initial Template for Python 3

t = int (input ())
for tc in range(t):
    n = int (input ())
    arr = list(map(int, input().split()))
    ob = Solution()
    print (ob.closestToZero (arr, n))
# } Driver Code Ends