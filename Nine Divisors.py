class Solution:
    def nineDivisors(self, N):
        c = 0
        limit = int(N ** (0.5))
        # Sieve array, initially prime[i] = i
        prime = [i for i in range(limit + 1)]
        # use sieve concept to store the
        # first prime factor of every number
        i = 2
        while i * i <= limit:
            if prime[i] == i:

                # mark all factors of i
                for j in range(i * i, limit + 1, i):
                    if prime[j] == j:
                        prime[j] = i
            i += 1
        # check for all numbers if they
        # can be expressed in form p*q
        for i in range(2, limit + 1):

            # p prime factor
            p = prime[i]

            # q prime factor
            q = prime[i // prime[i]]

            # if both prime factors are different
            # if p*q<=n and q!=
            if p * q == i and q != 1 and p != q:
                c += 1
            elif prime[i] == i:

                # Check if it can be
                # expressed as p^8
                if i ** 8 <= N:
                    c += 1
        return c

    # {


# Driver Code Starts
# Initial Template for Python 3
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        print(ob.nineDivisors(N))

# } Driver Code Ends