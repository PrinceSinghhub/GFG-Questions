# User function Template for python3

class Solution:
    def findTwoElement(self, a, n):
        a.sort()
        exp = (len(a) * (len(a) + 1)) // 2
        mysum = 0

        for i in a:
            mysum += i
        for i in range(len(a) - 1):
            if a[i + 1] - a[i] == 0:
                B = a[i]
        if mysum > exp:
            A = B - (mysum - exp)
        else:
            A = B + (exp - mysum)

        return B, A

        # bruteforce Approch
        # ans = []

        # for i in arr:
        #     if arr.count(i)>1:
        #         ans.append(i)
        #         break

        # for j in range(1,n+1):
        #     if j not in arr:
        #         ans.append(j)
        #         break

        # return ans