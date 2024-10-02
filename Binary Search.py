class Solution:
    def binarysearch(self, arr, n, k):

        start = 0
        end = n - 1

        while start <= end:
            mid = start + (end - start) // 2

            if arr[mid] == k:
                return mid

            if arr[mid] > k:
                end = mid - 1

            if arr[mid] < k:
                start = mid + 1

        return -1


# {
#  Driver Code Starts
# Initial template for Python

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split(' ')))
        k = int(input())
        ob = Solution()
        print(ob.binarysearch(arr, n, k))