#User function Template for python3

class Solution:
    def digitsNum(self, N):
        return (str(N%9)+(N//9)*"9"+N*"0") if (N%9!=0) else ((N//9)*"9"+N*"0")


#{
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		ob = Solution()
		ans = ob.digitsNum(n)
		print(ans)
# } Driver Code Ends