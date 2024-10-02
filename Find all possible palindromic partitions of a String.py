class Solution:
    def allPalindromicPerms(self, S):
        # code here
        def func(index, s, path, res):
            if index == len(s):
                res.append([ele for ele in path])
                return
            for i in range(index, len(s)):
                if isPalindrome(s, index, i):
                    path.append(s[index:i + 1])
                    func(i + 1, s, path, res)
                    path.pop()

        def isPalindrome(s, start, end):
            while start <= end:
                if s[start] != s[end]:
                    return False
                start += 1
                end -= 1
            return True

        res = []
        path = []
        func(0, S, path, res)
        return res


# {
# Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        S = input()

        ob = Solution()
        allPart = ob.allPalindromicPerms(S)
        for i in range(len(allPart)):
            for j in range(len(allPart[i])):
                print(allPart[i][j], end=" ")
            print()
            # } Driver Code Ends