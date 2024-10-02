class Solution:
    def Count(self, L, R):
        a = [True]*(R+1)
        a[1] = False
        i = 2
        while i*i <=R:
            if a[i]:
                j = i*i
                while j<=R:
                    a[j] = False
                    j += i
            i = i+1
        prime = 0
        for i in range(max(2,L),R+1):
            if a[i]:
                prime += 1
        return (R-max(2,L)+1)-2*prime