class Solution:
    def partition(self, arr, low, high):
        pivot = arr[low]
        left = low + 1
        right = high

        while True:
            while left <= right and arr[left] <= pivot:
                left = left + 1
            while left <= right and arr[right] >= pivot:
                right = right - 1
            if right < left:
                break
            else:
                arr[left], arr[right] = arr[right], arr[left]

        arr[low], arr[right] = arr[right], arr[low]
        return right

    def quickSort(self, arr, low, high):
        if low <= high:
            a = self.partition(arr, low, high)
            self.quickSort(arr, low, a - 1)
            self.quickSort(arr, a + 1, high)


# {
#  Driver Code Starts
# Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        Solution().quickSort(arr, 0, n - 1)
        for i in range(n):
            print(arr[i], end=" ")
        print()