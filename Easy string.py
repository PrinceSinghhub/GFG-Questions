class Solution:

    def transform(self, S):
        S=S.lower()
        i=0
        j=1
        ans=''
        count=1
        if len(S)==1:
            ans+=str(count)+S[0]
            return ans
        while i<len(S) or j<len(S):
            if S[i]==S[j]:
                count+=1
                if j==len(S)-1:
                    ans+=str(count)+S[i]
                    break
                j+=1
            else:
                ans+=str(count)+S[i]
                count=1
                i=j
                if j==len(S)-1:
                    ans+=str(count)+S[j]
                    break
                j+=1
        return ans


#{
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        S = input()

        solObj = Solution()

        print(solObj.transform(S))
# } Driver Code Ends