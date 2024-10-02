class Solution:

    def fascinating(self, n):

        mul3 = n * 3
        mul2 = n * 2

        ans = str(n) + str(mul2) + str(mul3)

        if len(ans) == 9:
            for i in range(1, 10):
                if ans.count(str(i)) == 1:
                    continue
                else:
                    return False
            return True

        else:
            return False


# {
#  Driver Code Starts
# Initial Template for Python 3


if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input().strip())
        ob = Solution()
        ans = ob.fascinating(n)
        if ans:
            print("Fascinating")
        else:
            print("Not Fascinating")
        tc -= 1