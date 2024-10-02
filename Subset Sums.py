#User function Template for python3
class Solution:
    
    def findAllSubset(self,ind,n,arr,ans,sum):
        
        if ind == n:
            ans.append(sum)
            return 

    
        self.findAllSubset(ind+1,n,arr,ans,sum+arr[ind])
        self.findAllSubset(ind+1,n,arr,ans,sum)
        
	def subsetSums(self, arr, N):
		# code here
        ans = []
        self.findAllSubset(0,N,arr,ans,0)
        ans.sort()
        return ans

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        N = int(input())
        arr = [int(x) for x in input().split()]
        ob = Solution()
        ans = ob.subsetSums(arr, N)
        ans.sort()
        for x in ans:
            print(x,end=" ")
        print("")

# } Driver Code Ends