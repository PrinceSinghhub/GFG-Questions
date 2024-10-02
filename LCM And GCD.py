class Solution:
    def hcf(self,a,b):

        if a == 0:
            return b

        return self.hcf(b%a,a)

    def lcm(self,a,b):

        return a*b // self.hcf(a,b)




    def lcmAndGcd(self, A , B):

        return [self.lcm(A,B),self.hcf(A,B)]

ans = Solution()
print(ans.lcmAndGcd(10,5))