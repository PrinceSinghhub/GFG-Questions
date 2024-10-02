class Solution:
    def zero_count(self, x):
        denome = 5
        zeros = 0
        while (x >= denome):
            zeros += (x // denome)
            denome *= 5
        return zeros

    def findNum(self, n: int):
        # Complete this function
        low = 0
        high = n * 5
        ans = low
        while (low <= high):
            mid = (low + high) // 2
            zeros = self.zero_count(mid)
            if (zeros >= n):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return ans


# {
#  Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())

    for _ in range(t):
        n = int(input())
        ob = Solution()
        print(ob.findNum(n))
# } Driver Code Ends