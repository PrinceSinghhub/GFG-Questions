class Solution:
    def gfSeries(self, N: int) -> None:
        # code here
        for i in range(1, N + 1):
            if i == N:
                print(self.helper(i))
                break
            print(self.helper(i), end=' ')

    def helper(self, N):
        if (N == 1):
            return 0
        if (N == 2):
            return 1;
        return self.helper(N - 2) * self.helper(N - 2) - self.helper(N - 1)


# {
# Driver Code Starts
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        N = int(input())

        obj = Solution()
        obj.gfSeries(N)

# } Driver Code Ends