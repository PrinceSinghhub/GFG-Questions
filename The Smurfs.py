class Solution:
    def minFind(self, n, a):
        i = 0
        r, g, b = 0, 0, 0
        while i < n:
            if a[i] == "R":
                r += 1
            elif a[i] == "G":
                g += 1
            elif a[i] == "B":
                b += 1
            i += 1
        if r % 2 == 0 and g % 2 == 0 and b % 2 == 0:
            return 2
        if r % 2 != 0 and g % 2 != 0 and b % 2 != 0:
            return 2
        else:
            return 1


# {
# Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = input().split()

        ob = Solution()
        print(ob.minFind(n, a))
# } Driver Code Ends