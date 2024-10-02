def rotate(self, N, D):
    d = D % 16
    res = [0, 0]
    temp = N
    mask = (1 << d) - 1
    shift = temp & mask
    temp >>= d
    temp += shift << (16 - d)
    res[1] = temp

    temp = N
    mask = ~((1 << (16 - d)) - 1)
    shift = temp & mask
    temp = temp << d
    temp += shift >> (16 - d)
    res[0] = temp

    mask = (1 << 16) - 1
    res[0] = res[0] & mask

    return res


# {
#  Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, d = input().strip().split(" ")
        n, d = int(n), int(d)
        ob = Solution()
        ans = ob.rotate(n, d)
        print(ans[0])
        print(ans[1])
# } Driver Code Ends