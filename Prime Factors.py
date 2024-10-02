#User function Template for python3

class Solution:
	def AllPrimeFactors(self, N):
 # Code here
         l = []
         p = 2
         while N != 1:
             if N%p == 0:
                 N //= p
                 l.append(p)
                 continue
             else:
                 p += 1
         l = sorted(list(set(l)))
         return l


#{
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		N = int(input())
		ob = Solution()
		ans = ob.AllPrimeFactors(N)
		for _ in ans:
			print(_, end = " ")
		print()
# } Driver Code Ends