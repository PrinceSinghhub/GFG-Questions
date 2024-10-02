class Solution:
    def FirstNonRepeating(self, A):
        uniqueList = []
        repeatedList = []
        sol = ""

        for i, c in enumerate(A):
            try:  # if c in uniqueList
                uniqueList.remove(c)
                repeatedList.append(c)
            except:
                if c not in repeatedList:
                    uniqueList.append(c)

            if uniqueList:
                sol += uniqueList[0]
            else:
                sol += '#'

        return sol


# {
#  Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        A = input()
        ob = Solution()
        ans = ob.FirstNonRepeating(A)
        print(ans)