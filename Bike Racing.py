class Solution:
    def buzzTime(self, N, M, L, H, A):

        low = 0
        high = max(L, M)
        ans = 0

        while low <= high:

            mid = (low + high) // 2

            fast = 0

            for i in range(N):
                if H[i] + A[i] * mid >= L:
                    fast += H[i] + A[i] * mid

            if (fast >= M):
                ans = mid
                high = mid - 1

            else:
                low = mid + 1

        return ans

ans = Solution()
N = 3
M = 400
L = 120
H = [20, 50, 20]
A = [20, 70, 90]
print(ans.buzzTime(N,M,L,H,A))
