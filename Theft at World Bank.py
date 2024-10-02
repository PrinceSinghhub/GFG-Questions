import math
class Solution:
	def maximumProfit(self, n, c, w, p):

        arr = []
        for i in range(n):
            if p[i] != 0:
                arr.append([w[i],p[i],w[i]/p[i]])
            else:
                arr.append([w[i],p[i],999999999])
        arr.sort(key = lambda x:x[2])
        ans = 0
        for i in range(n):
            if c == 0:
                break
            if math.sqrt(arr[i][0]) % 1 == 0:
                continue
            if c>= arr[i][0]:
                c-=arr[i][0]
                ans += arr[i][1]
            else:
                ans += (arr[i][1]/arr[i][0]) * c
                break
        return ans

ans = Solution()
n = 3
c = 10
print(ans.maximumProfit(n,c,w,p))
