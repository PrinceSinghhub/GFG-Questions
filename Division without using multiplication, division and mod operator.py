class Solution:
    def divide(self, a, b):

        ans = a // b + (a % b != 0) * ((a < 0) ^ (b < 0))
        return ans

        if b < 0:
            b = b * -1
            ans = a // b
            return ans * -1
        else:
            return a // b

        # if b < 0:

        #     b = -1*b
        #     div = b
        #     ans = 1
        #     while div <= a:
        #         ans+=1

        #     ans = ans-1
        #     return ans*-1

        # else:

        #     div = b
        #     ans = 1

        #     while div <= a:
        #         div+=b
        #         ans+=1

        #     return ans-1

        # code here


# {
#  Driver Code Starts
# Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    for _ in range(0, t):
        inp = list(map(int, input().split()))

        a = inp[0]
        b = inp[1]

        ob = Solution()

        print(ob.divide(a, b))

# } Driver Code Ends