from typing import List

class Solution:

    def maxLevel(self, h:int,m:int) -> int:
        f1,c = 0,0
        while h>0 and m>0:
            if f1!=1:
                h+=3
                m+=2
                f1=1
            elif m>10 and h>5:
                f1=0
                h-=5
                m-=10
            elif h>20:
                f1=0
                h-=20
                m+=5
            else:
                break
            c+=1
        return c