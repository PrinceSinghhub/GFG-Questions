class Solution:
    def makeProductOne(self, arr, N):
        p = 0
        n = 0
        z = 0
        step = 0
        for i in range(len(arr)):
            if (arr[i] == 0):
                z += 1
            elif (arr[i] < 0):
                n += 1
                step = step + (-1 - arr[i])
            else:
                p += 1
                step = step + (arr[i] - 1)
        if (n % 2 == 0):
            step = step + z
        else:
            if (z > 0):
                step = step + z
            else:
                step = step + 2
        return step


# {
# Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        arr = list(map(int, input().split()))

        ob = Solution()
        print(ob.makeProductOne(arr, N))
# } Driver Code Ends