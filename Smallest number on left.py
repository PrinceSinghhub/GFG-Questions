# User function Template for Python3

class Solution:
    def leftSmaller(self, n, a):
        ans = [-1] * n
        st = []
        for i in range(len(a)):
            while st and a[st[-1]] >= a[i]:
                st.pop()
            if st:
                ans[i] = a[st[-1]]
            st.append(i)
        return ans


# {
# Driver Code Starts
# Initial Template for Python3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = input().split()
        for i in range(n):
            a[i] = int(a[i])

        ob = Solution()
        ans = ob.leftSmaller(n, a)
        for u in (ans):
            print(u, end=" ")
        print()
# } Driver Code Ends