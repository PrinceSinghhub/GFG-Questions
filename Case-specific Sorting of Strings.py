class Solution:

    #Function to perform case-specific sorting of strings.
    def caseSort(self,s,n):
        S = s
        lower =""
        upper =""
        for i in S:
            if i.islower():
                lower+=i
            else:
                upper+=i

        lower=sorted(lower)
        upper =sorted(upper)
        res = lower+upper
        llen = len(lower)

        k = 0
        final =""
        for i in S:
            if i.islower():
                final+=res[k]
                k+=1
            elif i.isupper():
                final+=res[llen]
                llen+=1
        return final

#{
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for tt in range(t):
        n=int(input())
        s=str(input())
        print(Solution().caseSort(s,n))