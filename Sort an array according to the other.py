# User function Template for python3

class Solution:
    # A1[] : the input array-1
    # N : size of the array A1[]
    # A2[] : the input array-2
    # M : size of the array A2[]

    # Function to sort an array according to the other array.
    def relativeSort(self, A1, N, A2, M):
        # Your Code Here
        d = {}
        for i in A1:
            d[i] = d.get(i, 0) + 1
        l = []
        l2 = []
        for i in A2:
            if i in d.keys():
                l += [i] * (d[i])
                del d[i]
        l2 = []
        for i, j in d.items():
            l2 += [i] * j
        l2.sort()
        l += l2
        return l


# {
#  Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    while t > 0:
        n, m = list(map(int, input().split()))
        a1 = list(map(int, input().split()))
        a2 = list(map(int, input().split()))

        ob = Solution()
        a1 = ob.relativeSort(a1, n, a2, m)
        print(*a1, end=" ")

        print()

        t -= 1

# } Driver Code Ends