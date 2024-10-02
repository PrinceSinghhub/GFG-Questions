# User function Template for python3

class Solution:

    def minRepeats(self, a, b):
        ans = 0
        j = 0
        i = 0
        for i in range(len(a)):
            if (b[0] == a[i]):
                break
        if (i == len(a)): return -1
        while (j < len(b)):
            if (i == len(a)):
                ans += 1
                i = 0
            if (a[i] != b[j]):
                return -1
            if (a[i] == b[j]):
                i += 1
                j += 1
        return ans + 1


# {
# Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        A = input()
        B = input()

        ob = Solution()
        print(ob.minRepeats(A, B))
# } Driver Code Ends