class Solution:
    def onesComplement(self, N):

        Bin = str(int(bin(N)[2::]))

        ans = ""
        for i in Bin:
            if i == "0":
                ans += "1"
            else:
                ans += "0"

        return int(ans, 2)

ans  = Solution()
print(ans.onesComplement(100))