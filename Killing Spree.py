class Solution:
    def killinSpree(self, n):
        # code here
        low = 0
        high = n
        mid = (low + high) // 2
        mid_pre = mid
        if (n < 1):
            return 0
        elif (n < 4):
            return 1
        elif (n == 13):
            return 2
        while low < high:  # find two immediate term in binary search between them the result lies

            sum_ = sum_triple(mid)
            if (sum_ > n):
                high = mid
                mid_pre = mid
                mid = (low + high) // 2
            else:
                k = final(mid, mid_pre, n)
                return k


def sum_triple(num):  # TO calculate the sum upto nth term
    k = int((num * (num + 1) * (2 * num + 1)) / 6)
    return k


def final(mid, mid_pre, n):  # apply linear search to find the result for immediate term.
    for i in range(mid_pre, mid - 1, -1):
        if (sum_triple(i) <= n):
            return i


# {
#  Driver Code Starts
# Initial Template for Python 3


if __name__ == '__main__':
    ob = Solution()
    t = int(input())
    for _ in range(t):
        N = int(input())
        ans = ob.killinSpree(N);
        print(ans)

# } Driver Code Ends