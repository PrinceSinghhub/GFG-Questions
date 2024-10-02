class Solution:
    def prime_Sum(self, n):

        if n < 2:
            return 0

    ans = 0
    for i in range(2, n + 1):

        count = 2
        flag = True

        while count * count <= i:
            if i % count == 0:
                flag = False
                break
            count += 1
        if flag == True:
            ans += i

    return ans


# {
#  Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        n = int(input())
        ob = Solution()
        ans = ob.prime_Sum(n)
        print(ans)