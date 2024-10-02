#User function Template for python3

class Solution:

     def longestKSubstr(self, s, k):
        m,c,ma = -1, "",{}
        for i in s:
            c += i
            # ma[i] = 1 + ma.get(ma[i],0)
            if i not in ma: ma[i] = 1
            else: ma[i] += 1
            if len(ma) == k: m = max(m,len(c))
            elif len(ma) > k:
                ma[c[0]] -= 1
                if ma[c[0]] == 0: del ma[c[0]]
                c = c[1:]
        return m


#{
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        s = input()
        k = int(input())

        solObj = Solution()

        ans = solObj.longestKSubstr(s, k)

        print(ans)

# } Driver Code Ends