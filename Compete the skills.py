class Solution:
    def scores(self, a, b, cc):

        for i in range(3):
            if (a[i] > b[i]):
                cc[0] = cc[0] + 1
            elif (a[i] < b[i]):
                cc[1] = cc[1] + 1
            else:
                continue
        return cc[0], cc[1]


# {
#  Driver Code Starts
# Initial Template for Python 3


def main():
    T = int(input())

    while (T > 0):
        a = [int(x) for x in input().strip().split()]
        b = [int(x) for x in input().strip().split()]

        cc = [0, 0]
        ob = Solution()
        ob.scores(a, b, cc)
        print(*cc)

        T -= 1


if __name__ == "__main__":
    main()