#User function Template for python3

class Solution:
    
    def findAllSubset(self,ind,n,arr,ans,temp):
        
        if ind == n:
            ans.append(temp[:])
            return 

        temp.append(arr[0])
        self.findAllSubset(ind+1,n,arr[1:],ans,temp)
        temp.pop()
        self.findAllSubset(ind+1,n,arr[1:],ans,temp)
        
        
    def subsets(self, arr):
        
        ans = []
        
        self.findAllSubset(0,len(arr),arr,ans,[])
        
        ans.sort()
        return ans
        

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        A = list(map(int,input().strip().split()))
        
        ob=Solution()
        result =ob.subsets(A)
        
        for i in range(len(result)):
            for j in range(len(result[i])):
                print(result[i][j],end=" ")
                
            print()
            
            

# } Driver Code Ends