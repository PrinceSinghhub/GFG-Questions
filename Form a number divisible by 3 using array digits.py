class Solution:
    def isPossible(self, N, arr):

        ans = 0
        for i in arr:
            ans += i % 3
        if ans % 3 == 0:
            return 1
        return 0

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        arr = input().split()
        for i in range(N):
            arr[i] = int(arr[i])

        ob = Solution()
        print(ob.isPossible(N, arr))


