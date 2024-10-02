
class Solution:
    def sum_of_square_oddNumbers(self, n):
        ans = 0

        old = 1

        for i in range(n):
            ans+= old * old
            old+=2
        return ans


# {
#  Driver Code Starts


if __name__ == '__main__':
    T=int( input())

    for i in range(T):
        n = int(input())
        ob = Solution();
        ans = ob.sum_of_square_oddNumbers(n)
        print(ans)
# } Driver Code Ends