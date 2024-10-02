class Solution:
    # Complete this function
    def power(self, n, r):
        # Your code here
        mod = 1000000007
        if r == 1:
            return n
        n = n % mod
        if r % 2 == 0:
            temp = self.power(n, r / 2) % mod
            return ((temp % mod) * (temp % mod)) % mod
        else:
            return (n * (self.power(n, r - 1) % mod)) % mod
# class Solution:
#
#     def power(self,N,R):
#         #Your code here

#         mod = 1000000007

#         ans = N ** R

#         return ans%mod