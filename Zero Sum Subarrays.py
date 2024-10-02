#User function Template for python3

class Solution:
    def findSubArrays(self,arr,n):
        for i in range(1,n):
            arr[i]+=arr[i-1]
        countmap={0:0}
        for item in arr:
            countmap[item]=1+countmap.get(item,0)
        tot=0
        for i in countmap.values():
            if i>1:
                tot+=((i*(i-1))//2)
        return (tot+countmap[0])


#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
        
if __name__=='__main__':
    t=int(input())
    for tc in range(t):
        
        N=int(input())
        A = [int(x) for x in input().strip().split(' ')]
        ob = Solution()
        print(ob.findSubArrays(A,N))
        
                
                
# } Driver Code Ends