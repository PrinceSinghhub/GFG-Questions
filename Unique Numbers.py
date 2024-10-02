#User function Template for python3
class Solution:
	def uniqueNumbers(self, L, R):
	    
	    ans = []
	    
	    for i in range(L,R+1):
	        
	        temp = str(i)
	        if len(temp) == len(set(temp)):
	            ans.append(i)
	    return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		l,r = input().split()
		l,r = int(l),int(r)
		
		ob = Solution()
		ans = ob.uniqueNumbers(l,r)
		for a in ans:
			print(a,end = ' ')
		print()

# } Driver Code Ends