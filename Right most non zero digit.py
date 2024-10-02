# User function Template for python3

class Solution:
    def rightmostNonZeroDigit(self, n, a):
        # code here
        cnt5 = 0
        cnt2 = 0
        r = 1
        for i in range(n):
            if a[i] == 0:
                r = 0
                break
            while a[i] % 5 == 0:
                a[i] = a[i] // 5
                cnt5 += 1
            while a[i] % 2 == 0:
                a[i] //= 2
                cnt2 += 1
            r = (r * a[i]) % 10
        if r == 0: return -1
        k = min(cnt2, cnt5)
        cnt2 -= k
        cnt5 -= k
        while cnt5 > 0:
            r = (r * 5) % 10
            cnt5 -= 1
        while cnt2 > 0:
            r = (r * 2) % 10
            cnt2 -= 1
        return r

    # {


# Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        A = list(map(int, input().split()))

        ob = Solution()
        print(ob.rightmostNonZeroDigit(n, A))
# } Driver Code Ends