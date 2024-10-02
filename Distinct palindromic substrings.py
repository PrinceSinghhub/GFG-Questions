# User function Template for python3

class Solution:
    def palindromeSubStrs(self, str):
        # code here
        l = len(str)
        ls = [0 for i in range(2 * l + 2)]
        a = '@#'
        for i in str:
            a += i
            a += '#'
        a += '@'
        s = set()
        for i in range(2, l * 2 + 2):
            while a[i - ls[i] - 1] == a[i + ls[i] + 1] and (a[i - ls[i] - 1] != '@' or a[i + ls[i] + 1] != '@'):
                ls[i] += 1
                if a[i] == '#' and ls[i] != 0:
                    m = (i // 2) - ls[i] // 2
                    n = (i // 2) + ls[i] // 2
                    b = str[m:n]
                    s.add(b)

                elif a[i] != '#' and ls[i] != 0:
                    m = i // 2 - ls[i] // 2 - 1
                    n = i // 2 + ls[i] // 2
                    b = str[m:n]
                    s.add(b)

                if a[i] != '#' and a[i] != '@' and ls[i] != 0:
                    s.add(a[i])

        if '' in s:
            s.remove('')
        return len(s)

    # {


# Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        Str = input()

        solObj = Solution()

        print(solObj.palindromeSubStrs(Str))
# } Driver Code Ends