class Solution:
    def checkMirrorTree(self, n, e, A, B):
        dictA = {}
        dictB = {}
        for x in range(0, 2 * e, 2):
            if A[x] in dictA:
                dictA[A[x]].append(A[x + 1])
            else:
                dictA[A[x]] = [A[x + 1]]
            if B[x] in dictB:
                dictB[B[x]].append(B[x + 1])
            else:
                dictB[B[x]] = [B[x + 1]]
        for x in dictA:
            if dictA[x] != list(reversed(dictB[x])):
                return 0
        return 1


# {
#  Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, e = map(int, input().split())

        A = list(map(int, input().split()))
        B = list(map(int, input().split()))

        ob = Solution()
        print(ob.checkMirrorTree(n, e, A, B))