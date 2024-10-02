# {
# Driver Code Starts
import math


# } Driver Code Ends
# Complete this function

class Solution:
    def josephus(self, n, k):
        a = []
        for i in range(1, n + 1):
            a.append(i)
        i = 0
        while True:
            if (i + 1) % k == 0:
                i += 1
            else:
                a.append(a[i])
                i += 1
            if i >= len(a):
                break
        return a[-1]


# {
# Driver Code Starts.

def main():
    T = int(input())

    while (T > 0):
        nk = [int(x) for x in input().strip().split()]
        n = nk[0]
        k = nk[1]

        print(Solution().josephus(n, k))

        T -= 1


if __name__ == "__main__":
    main()
# } Driver Code Ends