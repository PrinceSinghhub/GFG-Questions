class Solution:
    def findPeakElement(self, a):
        return max(a)


# {
#  Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        n = int(input())
        a = list(map(int, input().split()))
        ob = Solution();
        ans = ob.findPeakElement(a)
        print(ans)