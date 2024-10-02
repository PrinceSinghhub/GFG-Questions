class Solution:

    def carpetBox(self, a, b, c, d):

        # code here

        m = 0

        w = 0

        l1, l2 = a, b

        while a > c:
            a //= 2

            m += 1

        while b > d:
            b //= 2

            m += 1

        a, b = l2, l1

        while a > c:
            a //= 2

            w += 1

        while b > d:
            b //= 2

            w += 1

        return min(m, w)


# {
# Driver Code Starts
# Initial Template for Python 3

def main():
    T = int(input())
    while (T > 0):
        A, B, C, D = map(int, input().split())

        obj = Solution()
        print(obj.carpetBox(A, B, C, D))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends