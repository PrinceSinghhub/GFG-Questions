class Solution:
    def findMidSum(self, ar1, ar2, n):
        ar1.extend(ar2)
        ar1.sort()

        mid = (len(ar1) - 1) // 2

        return ar1[mid] + ar1[mid + 1]


# {
#  Driver Code Starts
# Initial Template for Python 3

if __name__ == "__main__":
    tc = int(input())
    while tc > 0:
        n = int(input())
        ar1 = list(map(int, input().strip().split()))
        ar2 = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.findMidSum(ar1, ar2, n)
        print(ans)
        tc = tc - 1