class Solution:
    def reversedBits(self, X):
        # code here

        mybin = bin(X)
        mybin = mybin[2::]

        cost = 32 - len(mybin)

        ans = ""

        for i in range(cost):
            ans += '0'

        ans += mybin
        ans = ans[::-1]

        return int(ans, 2)


# {
#  Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        X = int(input())

        ob = Solution()
        print(ob.reversedBits(X))