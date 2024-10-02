class Solution:
    def isLucky(self, n):
        # RETURN True OR False

        i = 2
        while n >= i:
            if n % i == 0:
                return False
            n = n - (n // i)
            i += 1
        return True


# {
#  Driver Code Starts
# Initial Template for Python 3

# contributed by RavinderSinghPB

if __name__ == '__main__':
    t = int(input())

    for tcs in range(t):
        n = int(input())
        obj = Solution()
        if obj.isLucky(n):
            print(1)
        else:
            print(0)