class Solution:
    def wordBreak(self, n, dic, s):
        ans=[]
        def fun(i,st):
            if i==len(s):
                ans.append(st[:-1])
                return
            for j in range(i,len(s)+1):
                if s[i:j] in dic:
                    fun(j,st+s[i:j]+' ')
        fun(0,'')
        return ans