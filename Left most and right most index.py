class Solution:

    def findIndex(self, arr, x, boll):

        start = 0
        end = len(arr) - 1

        ans = -1

        while start <= end:
            mid = start + (end - start) // 2

            if x > arr[mid]:
                start = mid + 1

            if x < arr[mid]:
                end = mid - 1

            if x == arr[mid]:

                ans = mid
                if boll == True:
                    end = mid - 1

                else:
                    start = mid + 1
        return ans

    def indexes(self, arr, x):
        ans = [-1, -1]

        first = self.findIndex(arr, x, True)
        last = self.findIndex(arr, x, False)

        ans[0] = first
        ans[1] = last

        return ans


# {
#  Driver Code Starts
# Initial Template for Python 3

def main():
    T = int(input())

    while (T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        k = int(input())
        obj = Solution()
        ans = obj.indexes(a, k)
        if ans[0] == -1 and ans[1] == -1:
            print(-1)
        else:
            print(ans[0], end=' ')
            print(ans[1])

        T -= 1


if __name__ == "__main__":
    main()
