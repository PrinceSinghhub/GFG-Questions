# User function Template for python3

class Solution:
    def sumMatrix(self, n, q):

        if (q > 2 * n):
            return 0
        if (q > n + 1):

            return (2 * n) - q + 1

        else:

            return q - 1

        # brute force Approch
        # arr = [[i for i in range(2,n+2)]]

        # for i in range(n-1):
        #     temp = []
        #     for j in arr[i]:
        #         temp.append(j+1)
        #     arr.append(temp)

        # count = 0

        # for i in arr:
        #     if q in i:
        #         count+=1
        # return count

ans = Solution()
print(ans.sumMatrix(10,5))