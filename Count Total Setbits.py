
# class Solution:
#     def countBits(self, N : int) -> int:

#         count = 0
#         for i in range(1,N+1):
#             bits = bin(i)[2::]
#             ans = bits.count('1')
#             count += ans
#         return count
#         # code here


class Solution:
    def countBits(self, n : int) -> int:
        count = 0
        pos = 0
        while (1 << pos) <= N:
            ones = (N + 1) // (1 << (pos + 1)) * (1 << pos)
            rem = max(0, (N + 1) % (1 << (pos + 1)) - (1 << pos))
            count += ones + rem
            pos += 1
        return count


# {
# Driver Code Starts
if __name_ _= ="__main__":
    t = int(input())
    for _ in range(t):

        N = int(input())

        obj = Solution()
        res = obj.countBits(N)

        print(res)


# } Driver Code Ends