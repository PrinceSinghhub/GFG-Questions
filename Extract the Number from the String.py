class Solution:
    def ExtractNumber(self,sen):
        x = sen.split(" ")
        v = -1
        for i in x:
            if i.isnumeric() and "9" not in i and int(i)>v:
                    v = int(i)
        return v


#{
 # Driver Code Starts
t = int(input())
for _ in range(t):
    S = input()
    ob = Solution()
    ans = ob.ExtractNumber(S)
    print(ans)

# } Driver Code Ends