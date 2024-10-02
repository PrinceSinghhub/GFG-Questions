class Solution:
    def getPairsCount(self, arr, n, k):
        dic = {}
        ans = 0

        for i in arr:
            sum = k - i
            if sum in dic:
                ans += dic[sum]
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1
        return ans

    # {


#  Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, k = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.getPairsCount(arr, n, k)
        print(ans)
        tc -= 1