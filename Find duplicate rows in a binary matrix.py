class Solution:
    def repeatedRows(self, arr, m ,n):
        s=set()
        ans=[]
        for i in range(m):
            row=0
            for item in arr[i]:
                row=(row<<1)+item
            if row in s:
                ans.append(i)
            else:
                s.add(row)
        return ans