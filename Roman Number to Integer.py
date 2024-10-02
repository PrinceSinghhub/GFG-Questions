class Solution:
    def romanToDecimal(self, S):

        map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

        num = map[S[0]]

        for i in range(1, len(S)):
            if map[S[i - 1]] < map[S[i]]:
                num += map[S[i]] - 2 * map[S[i - 1]]
            else:
                num += map[S[i]]

        return num


# {
#  Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        ob = Solution()
        S = input()
        print(ob.romanToDecimal(S))