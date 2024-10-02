class Solution:
    def sum_of_square_evenNumbers(self, n):
        num = 2
        sum = 0

        for i in range(1, n + 1):
            sum += num * num
            num = num + 2

        return sum

    # ans = 0

    # even = 2

    # for i in range(n):
    #     temp = even ** 2
    #     ans+=temp
    #     even+=2
    # return ans


# {
#  Driver Code Starts
if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        n = int(input())
        ob = Solution();
        ans = ob.sum_of_square_evenNumbers(n)
        print(ans)
# } Driver Code Ends