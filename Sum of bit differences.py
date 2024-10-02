# User function Template for python3
class Solution:

    def sumBitDifferences(self, arr, n):
        count = 0

    for i in range(32):
        count_set = 0
        for num in arr:
            if (num >> i & 1) == 1:
                count_set += 1

        count += (count_set * (n - count_set)) * 2

    return count


# code here


# {
# Driver Code Starts

# Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.sumBitDifferences(arr, n)
        print(ans)
        tc -= 1

# } Driver Code Ends