class Solution:
    def findOnce(self, arr: list, n: int):
        low = 0
        high = n - 1

        while low < high:
            mid = low + (high - low) // 2

            if ((mid % 2 == 0 and arr[mid] == arr[mid + 1]) or
                    (mid % 2 != 0 and arr[mid] == arr[mid - 1])):
                low = mid + 1
            else:
                high = mid

        return arr[low]


# {
#  Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())

    for _ in range(t):
        n = int(input())
        arr = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.findOnce(arr, n))