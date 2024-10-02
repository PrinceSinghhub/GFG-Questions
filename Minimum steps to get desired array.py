class Solution:
    def countMinOperations(self, arr, n):

        m = 0
        sub = 0
        for i in range(n):
            temp = 0
            while arr[i] != 0:
                if arr[i] % 2 == 0:
                    arr[i] //= 2
                    temp += 1
                else:
                    sub += 1
                    arr[i] -= 1
            m = max(temp, m)
        return (m + sub)


# {
#  Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.countMinOperations(arr, n)
        print(ans)
        tc -= 1