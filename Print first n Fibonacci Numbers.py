class Solution:
    # Function to return list containing first n fibonacci numbers.
    def printFibb(self, n):
        ans = []

        first = 0
        second = 0
        third = 1

        for i in range(n):
            ans.append(third)
            first = second
            second = third
            third = first + second

        return ans


# {
#  Driver Code Starts
# Initial Template for Python 3


if __name__ == '__main__':
    t = int(input())
    for tcs in range(t):

        n = int(input())
        res = Solution().printFibb(n)
        for i in range(len(res)):
            print(res[i], end=" ")
        print()