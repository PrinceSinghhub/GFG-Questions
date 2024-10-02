class Solution:
    ##Complete this function
    # Function to find number of bits needed to be flipped to convert A to B
    def countBitsFlip(self, a, b):
        mas = a ^ b
        ans = 0

        while mas != 0:
            mas = mas & mas - 1
            ans += 1

        return ans

ans = Solution()
a = 30
b = 20
print(ans.countBitsFlip(a,b))