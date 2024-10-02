from math import gcd
class Solution:
    def Count(self, nums, k):
     # Code here
        ans=0
        n=len(nums)
        m=(1<<n)
        for i in range(m):
            x=1
            c=0
            for j in range(n):
                if(i&(1<<j)):
                    c+=1
                    x=(x*nums[j])//gcd(x,nums[j])
            if not c:
                continue
            if c&1:
                ans+=(k//x)
            else:
                ans-=(k//x)
        return int(ans)
#{
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n, k = input().split()
		n = int(n); k = int(k);
		nums = list(map(int, input().split()));
		ob = Solution()
		ans = ob.Count(nums, k)
		print(ans)

# } Driver Code Ends