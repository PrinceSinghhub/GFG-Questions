class Solution:
    def minRepeats(self, A, B):

        a = len(A)
        b = len(B)
        h = a
        s = ""
        c = 0
        while a <= b:
            s = s + A
            a = a + h
            c = c + 1
        if B in s:
            return c
        elif B in s + A:
            return c + 1
        else:
            return -1


# {
#  Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        A = input()
        B = input()

        ob = Solution()
        print(ob.minRepeats(A, B))