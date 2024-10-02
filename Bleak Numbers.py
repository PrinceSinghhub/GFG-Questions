
class Solution:
	def is_bleak(self,n):
        for i in range(32):
            if i <= n and bin(n - i).count('1') == i:
                return 0
        return 1


