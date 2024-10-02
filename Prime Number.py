class Solution:
    def isPrime(self, N):
        # code here

        if N < 2:
            return 0

        count = 2

        while count * count <= N:

            if N % count == 0:
                return 0
            count += 1

        return 1


# {
#  Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())

        ob = Solution()
        print(ob.isPrime(N))