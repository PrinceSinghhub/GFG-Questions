class Solution:
    def findMax(self, N):
        arr = []

        for i in str(N):
            arr.append(int(i))
        arr.sort()

        arr = arr[::-1]

        ans = ""

        for i in arr:
            ans += str(i)

        return int(ans)


# {
#  Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = input()

        ob = Solution()
        print(ob.findMax(N))