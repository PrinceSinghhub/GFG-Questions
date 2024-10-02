class Solution:
    def formCoils(self, n):
        arr = [[], []]
        n *= 4
        i1 = int(n / 2)
        j1 = i1 - 1
        i2 = int(n / 2) - 1
        j2 = i2 + 1
        sign = -1
        k = 2
        while 1:
            for _ in range(k):
                arr[0].append((n * i1) + j1 + 1)
                i1 += sign
                arr[1].append((n * i2) + j2 + 1)
                i2 += (sign * -1)
            if i1 == n:
                break
            for _ in range(k):
                arr[0].append((n * i1) + j1 + 1)
                j1 -= sign
                arr[1].append((n * i2) + j2 + 1)
                j2 -= (sign * -1)
            sign *= -1
            k += 2
        return arr


# {
#  Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())

        ob = Solution()
        ptr = ob.formCoils(n)

        for i in range(2):
            print(*ptr[i])
# } Driver Code Ends