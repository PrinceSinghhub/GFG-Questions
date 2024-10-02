class Solution:
    def quickSort(self, array):
        if len(array) <= 1:
            return array
        # base-case
        pivot = array.pop()
        left = []
        right = []
        for item in array:
            if item < pivot:
                left.append(item)
            else:
                right.append(item)
        return (self.quickSort(left) + [pivot] + self.quickSort(right))

        def kLargest(self, arr, n, k):

            ans = self.quickSort(arr)
            ans = ans[::-1]
            return ans[:k]


# {
#  Driver Code Starts
# Initial Template for Python 3


if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, k = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.kLargest(arr, n, k)
        for x in ans:
            print(x, end=" ")
        print()
        tc -= 1