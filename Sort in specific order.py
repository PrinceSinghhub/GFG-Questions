class Solution:
    def sortIt(self, arr, n):
        ans = []

        old = []
        even = []

        for i in arr:
            if i % 2 != 0:
                old.append(i)
            else:
                even.append(i)

        old.sort()
        even.sort()

        ans.extend(old[::-1])
        ans.extend(even)

        arr[:] = ans
        return arr


# {
#  Driver Code Starts
# Initial Template for Python 3

def main():
    T = int(input())

    while (T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        ob = Solution()
        ob.sortIt(a, n)
        print(*a)

        T -= 1


if __name__ == "__main__":
    main()