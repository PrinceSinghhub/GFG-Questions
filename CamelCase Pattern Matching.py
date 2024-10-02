class Solution:
    def CamelCase(self,N,Dictionary,Pattern):
        #code here
        li=[]
        for i in Dictionary:
            x=''
            for j in i:
                if j.isupper(): x+=j
            if Pattern==x[:len(Pattern)]:
                li.append(i)
        return li if len(li)!=0 else [-1]2