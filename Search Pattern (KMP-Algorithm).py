class Solution:
    def search(self, pat, txt):
        # code here
        res=[]
        lenpat=len(pat)
        for i in range(0,len(txt)):
            if txt[i:lenpat+i]==pat:
                res.append(i+1)
        if res:
            return res
        else:
            return [-1]
