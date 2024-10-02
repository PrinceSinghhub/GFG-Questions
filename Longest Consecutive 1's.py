class Solution:
    ##Complete this function
    # Function to calculate the longest consecutive ones
    def maxConsecutiveOnes(self, N):
        ##Your code here

        count = 0
        mx = 0

        while (N > 0):

            if N & 1:
                count += 1
                mx = max(mx, count)

            else:
                count = 0

            N = N >> 1
        return mx

ans = Solution()
a = 140
print(ans.maxConsecutiveOnes(a))

print(5 << 1)