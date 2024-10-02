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


# {
#  Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':

    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.findTwoElement(arr, n)
        print(str(ans[0]) + " " + str(ans[1]))
        tc = tc - 1
# } Driver Code Ends