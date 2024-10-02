class Solution:
    def find_median(self, v):
        x = len(v)
        v.sort()

        if x % 2 == 1:
            return v[x // 2]
        else:
            return ((v[(x - 1) // 2] + v[x // 2]) // 2)


# {
#  Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        n = int(input())
        v = list(map(int, input().split()))
        ob = Solution();
        ans = ob.find_median(v)
        print(ans)
# } Driver Code Ends