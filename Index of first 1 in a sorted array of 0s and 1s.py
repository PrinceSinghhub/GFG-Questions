class Solution:
    def firstIndex(self, arr, n):
        if 1 in arr:
            return arr.index(1)

        return -1
    # Your code goes here


# {
#  Driver Code Starts
# Initial Template for Python 3

def main():
    T = int(input())

    while (T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.firstIndex(a, n))

        T -= 1


if __name__ == "__main__":
    main()
