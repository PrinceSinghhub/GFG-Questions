# User function Template for python3
class Solution:
    def isPrime(self, n):
        if n < 2:
            return False
        if n == 2 or n == 3:
            return True
        if n % 2 == 0:
            return False
        if n % 3 == 0:
            return False

        limit = int(n ** 0.5)
        i = 5
        t = 2
        while i <= limit:
            if n % i == 0:
                return False
            i += t
            t = 6 - t
        return True

    def superPrimes(self, n):
        # code here
        if n < 5:
            return 0
        if n < 7:
            return 1
        count = 1
        i = 7
        while i <= n:
            if self.isPrime(i) and self.isPrime(i - 2):
                # print(i,i-2)
                count += 1
            i += 6

        return count


# {
#  Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        n = int(input())
        ob = Solution()
        ans = ob.superPrimes(n)
        print(ans)

# } Driver Code Ends