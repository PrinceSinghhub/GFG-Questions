class Solution:
    def findElements(self, a, n):
        a.sort()

        return a[0:n - 2]


# {
#  Driver Code Starts
# Initial Template for Python 3

def main():
    T = int(input())

    while (T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(*ob.findElements(a, n))

        T -= 1


if __name__ == "__main__":
    main()