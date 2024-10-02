# User function Template for python3

class Solution:
    def FirstNonRepeating(self, A):
        t = []

    t.append(A[0])
    ans = ""
    ans += A[0]
    temp = []
    temp.append(A[0])
    for i in range(1, len(A)):
        if A[i] not in temp:
            t.append(A[i])
            temp.append(A[i])
        elif A[i] in t:
            t.remove(A[i])

        if len(t) > 0:
            ans += t[0]
        else:
            ans += '#'

    return ans


# {
# Driver Code Starts

# Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        A = input()
        ob = Solution()
        ans = ob.FirstNonRepeating(A)
        print(ans)

# } Driver Code Ends