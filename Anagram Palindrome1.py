#User function Template for python3

class Solution:

     def isPossible(self, S):
        count = {}
        res = 0
        for i in S:
            if i not in count:
                count[i] = 1
            else:
                count[i] += 1
        for value in count.values():
            if value % 2 == 1:
                res += 1
        return 0 if res > 1 else 1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        S = input()

        solObj = Solution()

        if solObj.isPossible(S):
            print("Yes")
        else:
            print("No")
# } Driver Code Ends