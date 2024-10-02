from collections import Counter


class Solution:
    # Function to return the position of the first repeating element.
    def firstRepeated(self, arr, n):

        # arr : given array
        # n : size of the array

        mydic = Counter(arr)
        # print(mydic)

        # for i in range(n):
        #     if arr[i] not in mydic:
        #         mydic[arr[i]] = 1
        #     else:
        #         mydic[arr[i]] = mydic[arr[i]]+1

        for i in range(n):
            if mydic[arr[i]] > 1:
                return i + 1
        return -1


# {
#  Driver Code Starts
# Initial Template for Python 3

# contributed by RavinderSinghPB
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())

        arr = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.firstRepeated(arr, n))