from bisect import bisect_left


class Solution:
    def removeStudents(self, H, N):
        # code here
        ans = []
        for st in H:
            pi = bisect_left(ans, st)
            if pi >= len(ans):
                ans.append(st)
            else:
                ans[pi] = st
        return N - len(ans)


# {
# Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        H = list(map(int, input().split()))

        ob = Solution()
        print(ob.removeStudents(H, N))
# } Driver Code Ends