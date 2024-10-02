class Solution:
    def smallestpositive(self, array, n):

        array.sort()
        total = 1
        for i in array:
            if (total >= i):
                total += i
        return total
        # Your code goes here


# {
#  Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        array = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.smallestpositive(array, n))