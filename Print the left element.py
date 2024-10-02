class Solution:
    def leftElement(self, arr, n):
        arr.sort()
        mid = (n - 1) // 2

        return arr[mid]


# {
#  Driver Code Starts
# Initial Template for Python 3

def main():
    T = int(input())

    while (T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.leftElement(a, n))

        T -= 1


if __name__ == "__main__":
    main()