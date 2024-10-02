class Solution:
    def removals(self,arr, n, k):
        l = 0
		t = 999999999
		a = []
		arr.sort()
        for i in range(n):
		    f = 0
		    while arr[-i-1]-arr[f]>k:
		        f +=1
		    if(t>f+l):
		        t = f+l
		    l +=1
	    return t