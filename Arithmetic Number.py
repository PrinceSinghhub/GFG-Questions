class Solution:
    def inSequence(self, A, B, C):
        if (C == 0):
            if A == B:
                return (1)
            else:
                return (0)
        if (((B - A) / C) < 0):
            return (0)
        if ((B - A) % C == 0):
            return (1)

        return (0)


# {
#  Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        A, B, C = [int(x) for x in input().split()]

        ob = Solution();
        print(ob.inSequence(A, B, C))