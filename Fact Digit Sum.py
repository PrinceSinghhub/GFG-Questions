class Solution:
	def FactDigit(self, N):
		fact=[1]*(10)
		for i in range(1,10):
		    fact[i]=i*fact[i-1]
		res=""
		for i in range(9,0,-1):
		    if N>=fact[i]:
		        rem=N//fact[i]
		        res+=str(i)*rem
		        N%=fact[i]
		return res[::-1]


#{
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		N = int(input())
		ob = Solution()
		ans = ob.FactDigit(N)
		for _ in ans:
			print(_, end = "")
		print()
# } Driver Code Ends