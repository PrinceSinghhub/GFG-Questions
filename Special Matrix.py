class Solution:
	def FindWays(self, n, m, b):
		d = {}
		for i in b:
			k = str(i[0])+','+str(i[1])
			d[k] = 0
		if str(n)+','+str(m) in d or str(1)+','+str(1) in d:
			return 0
		def r(n,m,mo={}):
			k = str(n) + ',' + str(m)
			if m == 1 and n == 1:
				return 1
			if m == 0 or n == 0:
				return 0
			if k in d :
				return 0
			if k in mo:
				return mo[k]
			mo[k] =  (r(n-1,m,mo)+r(n,m-1,mo)) % (10**9+7)
			return mo[k]
		return r(n,m,{})

#{
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n, m, k= input().split()
		n = int(n); m = int(m); k = int(k);
		blocked_cells = []
		for i in range(k):
			a = list(map(int, input().split()))
			blocked_cells.append(a)
		obj = Solution()
		ans = obj.FindWays(n, m, blocked_cells)
		print(ans)