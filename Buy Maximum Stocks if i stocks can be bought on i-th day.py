from typing import List
class Solution:
    def buyMaximumProducts(self, n, k, price):
        l=[]
        for i in range(n):
            l.append((i+1,price[i]))
        l.sort(key=lambda item:item[1])
        count=0
        i=0
        while i<n and l[i][1]<=k:
            if k>=l[i][0]*l[i][1]:
                count+=l[i][0]
                k-=l[i][0]*l[i][1]
            else:
                count+=k//l[i][1]
                k%=l[i][1]
            i+=1
        return count