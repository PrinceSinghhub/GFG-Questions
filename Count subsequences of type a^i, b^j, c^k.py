class Solution:
    def fun(self,s):
        # code here
        arr = list(s)
        a = ab = abc = 0
        for i in range(len(arr)):
            if(arr[i] == 'a'):
                a = 2*a+1
            elif(arr[i] == 'b'):
                ab = 2*ab+a
            else:
                abc = 2*abc+ab
        return abc%1000000007