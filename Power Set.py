#User function Template for python3

class Solution:
    def AllPossibleStrings(self, s):
		# Code here
        ans = []
        def f(i,res):
            if i == len(s):
                return 
            res += s[i]
            ans.append(res)
            f(i+1, res)
            f(i+1, res[:-1])
            
            return
        f(0, '')
        ans.sort()
        return ans

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		s = input()
		ob = Solution();
		ans = ob.AllPossibleStrings(s)
		for i in ans:
			print(i, end = " ");
		print()
# } Driver Code Ends