import math
class Solution:
	def compute_value(self, n):
		t = math.factorial(n)
		return (math.factorial(2*n) // t // t) % (10**9+7)