class Solution:
    def findAndReplace(self, S, Q, index, sources, targets):
        # code here
        s1 = str(S[:])
        shift = 0
        for idx, source, target in zip(index, sources, targets):
            if S[idx:idx + len(source)] == source:
                idx = idx + shift
                s1 = s1[:idx] + target + s1[idx + len(source):]

                shift += len(target) - len(source)
        return s1


# {
#  Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        S = input()
        Q = int(input())
        index = list(map(int, input().split()))
        sources = list(map(str, input().split()))
        targets = list(map(str, input().split()))

        ob = Solution()
        print(ob.findAndReplace(S, Q, index, sources, targets))