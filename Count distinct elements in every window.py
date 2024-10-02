class Solution:

    def countDistinct(self, A, N, K):

        # Code here

        window_start = 0

        gg = {}

        ans = []

        for window_end in range(N):

            val = A[window_end]

            if val not in gg:

                gg[val] = 1

            else:

                gg[val] += 1

            if window_end >= K - 1:

                item = A[window_start]

                ans.append(len(gg))

                gg[item] -= 1

                if gg[item] <= 0:
                    del gg[item]

                window_start += 1

        return ans


# {
# Driver Code Starts
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n, k = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        res = Solution().countDistinct(arr, n, k)
        for i in res:
            print(i, end=" ")
        print()
# } Driver Code Ends