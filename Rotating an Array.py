class Solution:
    def leftRotate(self, arr, n, d):
        ro = arr[0:d]
        nr = arr[d:n]

        nr.extend(ro)
        arr[:] = nr
        return arr


# {
#  Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        d = int(input())
        ob = Solution()
        ob.leftRotate(arr, n, d)
        for xx in arr:
            print(xx, end=" ")
        print()
        tc -= 1