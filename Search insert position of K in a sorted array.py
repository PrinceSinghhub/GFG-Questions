class Solution:

    def searchInsertK(self, Arr, N, k):

        start = 0
        end = N - 1

        while start <= end:
            mid = start + (end - start) // 2

            if k == Arr[mid]:
                return mid

            elif k > Arr[mid]:
                start = mid + 1

            elif k < Arr[mid]:
                end = mid - 1

        return start


# {
#  Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        Arr = input().split()
        for itr in range(N):
            Arr[itr] = int(Arr[itr])
        k = int(input())
        ob = Solution()
        print(ob.searchInsertK(Arr, N, k))