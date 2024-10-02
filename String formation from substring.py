# User function Template for python3
class Solution:
    def isRepeat(self, s):
        ne = s + s
        new = ne[1:len(ne) - 1]
        f = new.find(s)
        if f != -1:
            return 1
        else:
            return 0


# {
#  Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        s = input()

        ob = Solution()
        answer = ob.isRepeat(s)

        print(answer)

# } Driver Code Ends