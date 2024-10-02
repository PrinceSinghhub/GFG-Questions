class Solution:
    def sumOfDivisors(self, N):
        sum=0
    	for i in range (1,N+1):
    	    if(N%i==0):
    	        for j in range (1,i+1):
    	            if(i%j==0):
    	                sum+=j
    	return sum

ans = Solution()
print(ans.sumOfDivisors(54))