import math
class Solution:
	def brainGame(self, nums):
		def Primefacto(n):
		    if n <= 1:
		        return 0
		    ans = 0
		    div = 2
		    while n > 1:
		        if n % div == 0:
		            ans += 1
		            n = n //div
		        else:
		            div += 1
		    return ans - 1
		arr = [Primefacto(num) for num in nums]
		s = 0
		for i in arr:
			s ^= i
        #print(s,arr)
		if s  != 0:
			return True
		else:
			return False