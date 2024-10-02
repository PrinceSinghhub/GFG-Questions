# User function Template for python3
class Solution:
    def toString(self, List):
        return ''.join(List)

    def permute(self, a, l, r, S):
        if l == r:
            S.append(self.toString(a))
            return;
        else:
            for i in range(l, r + 1):
                a[l], a[i] = a[i], a[l]
                self.permute(a, l + 1, r, S)
                a[l], a[i] = a[i], a[l]

    def permutation(self, s):
        n = len(s)
        a = list(s)
        S = []
        self.permute(a, 0, n - 1, S)
        S.sort()
        return S


# {
# Driver Code Starts
# Initial Template for Python 3

if __name__ == "__main__":
    T = int(input())
    while (T > 0):
        s = input()
        ob = Solution()
        ans = ob.permutation(s)
        for i in ans:
            print(i, end=" ")
        print()

        T -= 1
# } Driver Code Ends