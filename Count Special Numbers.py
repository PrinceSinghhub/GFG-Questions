# User function Template for python3

class Solution:
    def countSpecialNumbers(self, N, arr):

        max_element = max(arr)

        res = []
        for i in range(max_element + 1):
            res.append(0)

        for i in arr:
            if res[i] <= 1:
                for j in range(i, max_element + 1, i):
                    res[j] = res[j] + 1

        return sum(res[i] > 1 for i in arr)


# {
# Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':

    T = int(input())
    while T > 0:
        N = int(input())
        arr = [int(i) for i in input().split()]
        ob = Solution()
        print(ob.countSpecialNumbers(N, arr))

        T -= 1
# } Driver Code Ends