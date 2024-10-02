class Solution:
	def NBitBinary(self, N):
		# code here
		res = []
		def recursive(s,one,zero):
		    if (one+zero==N):
		        if s[0]!='0' and one>=zero:
		            res.append(s)
		        return 
            if(one<zero):
                return
	
            recursive(s+"1",one+1,zero)
            recursive(s+"0",one,zero+1)
		   
	
	    recursive("",0,0)
	    return res

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		ob = Solution()	
		answer = ob.NBitBinary(n)
		for value in answer:
			print(value,end=" ")
		print()


# } Driver Code Ends