class Solution:
    def minIteration(self, n, m, x, y):
        #code here
        lrud = [y-1, m-y, x-1, n-x] #left_right_up_down
        return  max(lrud[0], lrud[1]) + max(lrud[2], lrud[3])


#{
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		N, M = map(int,input().split())
		x, y = map(int,input().split())
		ob = Solution()
		print(ob.minIteration(N, M, x, y))
# } Driver Code Ends