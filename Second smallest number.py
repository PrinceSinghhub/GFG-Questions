# User function Template for python3

class Solution:

    def secondSmallest(self, S, D):

        ans = ["0"] * D

        if D * 9 <= S:
            return "-1"

        S = S - 1

        e = D - 1

        for i in range(D - 1, 0, -1):

            if S >= 9:

                ans[i] = "9"

                S = S - 9

                e = i

            else:

                ans[i] = str(S)

                S = 0

        ans[0] = str(1 + S)

        ans[e] = str(int(ans[e]) - 1)

        ans[e - 1] = str(int(ans[e - 1]) + 1)

        return ''.join(ans)


# {
# Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        S, D = map(int, input().strip().split(" "))

        ob = Solution()
        print(ob.secondSmallest(S, D))
# } Driver Code Ends