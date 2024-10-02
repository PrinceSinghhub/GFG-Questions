# User function Template for python3

class Solution:
    def unvisitedLeaves(self, N, leaves, frogs):
        # code here
        # frogs.sort()
        v = [0] * (leaves + 1)

        for i in range(N):
            if frogs[i] > leaves:
                continue
            if not v[frogs[i]]:
                for j in range(frogs[i], (leaves + 1), frogs[i]):
                    v[j] = 1
        ans = 0
        for i in v:
            ans += not i
        return ans - 1


# {
# Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':

    T = int(input())
    while T > 0:
        N, leaves = [int(i) for i in input().split()]
        frogs = [int(i) for i in input().split()]
        ob = Solution()
        print(ob.unvisitedLeaves(N, leaves, frogs))

        T -= 1
# } Driver Code Ends